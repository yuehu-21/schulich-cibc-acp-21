# -*- coding: utf-8 -*-

import pandas as pd
import getyahoofinance as gyf

df_stocklist = pd.read_csv('List of Stocks For An Exchange.csv', keep_default_na=False)
df_symbol = df_stocklist['Local Symbol']

list_key_executives = []
list_no_data = []
i_df_symbol = 1
for item_df_symbol in df_symbol:
    print('...Company Symbol: ' + item_df_symbol + ', Status: ' + str(i_df_symbol) + ' / ' + str(len(df_symbol)))
    try:
        dict_profile = gyf.yahoo_profile_scrape(item_df_symbol)
    except:
        try:
            dict_profile = gyf.yahoo_profile_scrape(item_df_symbol + '.TO')
            list_key_executives = list_key_executives + dict_profile['Key Executives']
        except:
            try:
                dict_profile = gyf.yahoo_profile_scrape(input('Please Verify the Symbol of ' + item_df_symbol + ' Manually: '))
                list_key_executives = list_key_executives + dict_profile['Key Executives']
            except:
                list_no_data.append(item_df_symbol)
    else:
        list_key_executives = list_key_executives + dict_profile['Key Executives']
    i_df_symbol += 1


df_key_executive_list = pd.DataFrame.from_dict(list_key_executives)

df_key_executive_list.to_csv('namelist.csv')
