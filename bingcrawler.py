# -*- coding: utf-8 -*-

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import random
from time import sleep
import getproxyip
from faker import Faker

df_namelist = pd.read_csv('namelist_canada_2.csv')

list_name_0 = []
list_name_1 = []
list_keyword = []
for i_df_namelist in range(len(df_namelist)):
    for j_df_namelist in range(i_df_namelist + 1, len(df_namelist)):
        list_name_0.append(df_namelist.loc[i_df_namelist, 'Name'])
        list_name_1.append(df_namelist.loc[j_df_namelist, 'Name'])
        list_keyword.append(df_namelist.loc[i_df_namelist, 'Name'] + ' and ' + df_namelist.loc[j_df_namelist, 'Name'])

df_names_0_1 = [pd.DataFrame(list_name_0), pd.DataFrame(list_name_1)]
df_names_0_1 = pd.concat(df_names_0_1, axis=1)
df_names_0_1.columns = ['name_0', 'name_1']

def searchingoogle(keyword, web_headers, proxy):
    bing_all = 'https://www.bing.com/search?q=KEYWORD'.replace('KEYWORD', keyword)
    bing_all_request = requests.get(bing_all, headers=web_headers, proxies=proxy)
    bing_all_soup = BeautifulSoup(bing_all_request.content, 'html.parser')
    
    if len(bing_all_soup.select('h1')[0].get_text()) == 0:
        search_results = bing_all_soup.select('div[id="b_tween"]')[0].get_text()
        try:
            search_results_match = re.match(r"(.*) results", search_results)
            search_amount = int(search_results_match.group(1).replace(',',''))
        except:
            search_amount = 0
    else:
        #if no results, set search_amount to 0
        search_amount = 0
    #The search amount from crawler might be different from the amount from browser, reason unknown
    sleep(random.uniform(0.01, 0.5))
    
    return search_amount


#define the search amount as the connections between 2 people
#a threshold will be given later to filter 'real' connection
fake = Faker()
df_connections = df_names_0_1.copy()
df_connections['Search Amount'] = 0
i_list_keyword = 0
#list_keyword = list_keyword[0 : 10]
for i_list_keyword in range(len(list_keyword)):
    print(str(i_list_keyword + 1) + ' / ' + str(len(list_keyword))  + ', ' + list_keyword[i_list_keyword])

    signal_proxy = 0
    while signal_proxy == 0:
        try:
            proxyip = getproxyip.pickproxyip()
            #proxy = {"http": proxyip, "https": proxyip}
            proxy = {"http": proxyip}
            web_headers ={'User-Agent':fake.user_agent()}
            df_connections.loc[i_list_keyword, 'Search Amount'] = searchingoogle(list_keyword[i_list_keyword], web_headers, proxy)
            signal_proxy = 1
            print('......' + list_keyword[i_list_keyword] + ' has been collected.')
        except:
            print('......connection failed, retry.')
            sleep(random.uniform(0.01, 0.5))


df_connections.to_csv('df_connections.csv')



