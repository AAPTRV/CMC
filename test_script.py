import pandas as pd
import numpy as np
import datetime
import time
import seaborn as sns
import data.collected_data.methods.get_listing_median_price as gt
import matplotlib.pyplot as plt

path_test = '/Users/eaxes/DA Projects/CMC/data/collected_data/coins_date_and_values'
path_to_csv = '/Users/eaxes/DA Projects/CMC/data/collected_data/mined/price_token_test.csv'

df = pd.read_csv(path_to_csv, index_col=0)

def get_median(coin_id):
    return gt.get_listing_sell_price(12, path_test, coin_id)

df['median_listing_price'] = df.apply(lambda x: get_median(df.coingecko_numerical_id), axis=1)

print(df)