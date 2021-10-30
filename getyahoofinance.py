# -*- coding: utf-8 -*-

#modified from:
#https://github.com/Jaydeeph/MakeMeMoney/blob/809ca2a560858f6559d94f9f18a218bb715fcc4a/python_scripts/yahoo_finance_scrape.py

import pandas as pd
import argparse
import math
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re

web_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36', 'Upgrade-Insecure-Requests': '1', 'Cookie': 'v2=1495343816.182.19.234.142', 'Accept-Encoding': 'gzip, deflate, sdch'}

ticker_summary = dict()
ticker_statistics = dict()
ticker_history = []
ticker_profile = dict()
ticker_analysis = dict()
ticker_holders = dict()

def yahoo_profile_scrape(ticker):
    yahoo_profile = 'https://finance.yahoo.com/quote/TICKER/profile?p=TICKER'.replace('TICKER', ticker)
    yahoo_profile_request = requests.get(yahoo_profile, headers=web_headers)
    yahoo_profile_soup = BeautifulSoup(yahoo_profile_request.content, 'html.parser')

    asset_profile = yahoo_profile_soup.select('div[data-test="asset-profile"]')[0]
    ticker_profile['Company Name'] = asset_profile.select('h3')[0].get_text()
    ticker_profile['Sector(s)'] = asset_profile.select('span[class="Fw(600)"]')[0].get_text()
    ticker_profile['Industry'] = asset_profile.select('span[class="Fw(600)"]')[1].get_text()
    ticker_profile['Full Time Exployees'] = asset_profile.select('span[class="Fw(600)"]')[2].get_text()
    ticker_profile['Description'] = yahoo_profile_soup.select('p[class="Mt(15px) Lh(1.6)"]')[0].get_text()

    basic_profile = asset_profile.select('p')[0].find_all(text=re.compile(""))
    list_basic_profile = []
    for item_basic_profile in basic_profile:
        if 'react-text:' not in str(item_basic_profile) and '/react-text' not in str(item_basic_profile):
            list_basic_profile.append(str(item_basic_profile))

    try:
        float(list_basic_profile[-2][0])
    except:
        ticker_profile['Company Address'] = ' '.join(list_basic_profile[0:-2])
        ticker_profile['Company Country'] = list_basic_profile[-2]
        ticker_profile['Company Phone'] = 'N/A'
        ticker_profile['Company Website'] = list_basic_profile[-1]
    else:
        ticker_profile['Company Address'] = ' '.join(list_basic_profile[0:-3])
        ticker_profile['Company Country'] = list_basic_profile[-3]
        ticker_profile['Company Phone'] = list_basic_profile[-2]
        ticker_profile['Company Website'] = list_basic_profile[-1]

    key_executive_table = yahoo_profile_soup.find_all("tbody")
    key_executives = []
    for table in key_executive_table:
        table_rows = table.find_all('tr')
        for table_row in table_rows:
            table_datas = table_row.find_all('td')

            key_executive = dict()
            key_executive['Name'] = table_datas[0].get_text()
            key_executive['Title'] = table_datas[1].get_text()
            key_executive['Pay'] = table_datas[2].get_text()
            key_executive['Exercised'] = table_datas[3].get_text()
            key_executive['Year Born'] = table_datas[4].get_text()
            key_executive['Company Name'] = ticker_profile['Company Name']
            key_executive['Yahoo Finance Code'] = ticker
            key_executive['Sector(s)'] = ticker_profile['Sector(s)']
            key_executive['Industry'] = ticker_profile['Industry']
            key_executive['Full Time Exployees'] = ticker_profile['Full Time Exployees']
            key_executive['Company Address'] = ticker_profile['Company Address']
            key_executive['Company Country'] = ticker_profile['Company Country']
            key_executive['Company Phone'] = ticker_profile['Company Phone']
            key_executive['Company Website'] = ticker_profile['Company Website']
            
            key_executives.append(key_executive)

    ticker_profile['Key Executives'] = key_executives

    return(ticker_profile)




