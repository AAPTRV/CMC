import pandas as pd


def get_df_tge():
    df = pd.read_csv('/Users/eaxes/DA Projects/CMC/data/collected_data/coins_date_and_values')
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%dT%H:%M:').dt.strftime('%Y-%m')
    return df.groupby(['coingecko_numerical_id']).agg({'date': 'min'})


def get_tge_for_coin(coingecko_numerical_id, df_tge):
    if df_tge.query(f"coingecko_numerical_id == {coingecko_numerical_id}")['date'].shape[0] > 0:
        return df_tge.query(f"coingecko_numerical_id == {coingecko_numerical_id}")['date'][0]
    else:
        return 'No tge'

df = pd.read_csv('/Users/eaxes/DA Projects/CMC/data/collected_data/mined/mined_table.csv').reset_index()
df_tge = get_df_tge().reset_index()
print(df_tge.head())
print(df.dtypes)
df_tge = df_tge.astype({'coingecko_numerical_id':'object'},errors='ignore')
print(df.dtypes)
print(df_tge.dtypes)


