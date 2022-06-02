import pandas as pd
import numpy as np
import parsing_scripts.scripts.daomaker as dm
import parsing_scripts.parsing_tools.coingecko.coingecko_listing as cg
from datetime import datetime

df = pd.read_csv('/Users/eaxes/DA Projects/CMC/data/collected_data/sample123.csv')
print(df.head())

id = df.iloc[0]['coingecko_numerical_id']

dict = cg.get_coin_chart(id)
for item in dict['stats']:
    item_date = datetime.utcfromtimestamp(item[0]/1000).strftime('%Y-%m-%d %H:%M')
    print(f"date:{item_date}")
    print(f"value:{item[1]}")
    print('***')


