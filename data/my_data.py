import pandas as pd
import numpy as np
import parsing_scripts.scripts.daomaker as dm
import parsing_scripts.parsing_tools.coingecko.coingecko_listing as cg

df = pd.read_csv('/Users/eaxes/DA Projects/CMC/data/collected_data/sample123.csv')
print(df.head())

id = df.iloc[0]['coingecko_numerical_id']

print(cg.get_coin_chart(id))

