import pandas as pd
import parsing_scripts.parsing_tools.coingecko.coingecko_listing as cg

dao_maker_df = pd.read_csv('/Users/eaxes/DA Projects/CMC/data/collected_data/sample123.csv')

df_values = pd.DataFrame(columns=['coingecko_numerical_id', 'date', 'value'])

for index, row in dao_maker_df.iterrows():
    coin_numerical_id = row['coingecko_numerical_id']

    if coin_numerical_id not in ['no-id', 'default']:
        print(row['coingecko_numerical_id'])
        result = cg.get_coin_chart_dataframe(coin_numerical_id)
        df_values = df_values.append(result, ignore_index=True)

df_values.to_csv('/Users/eaxes/DA Projects/CMC/data/collected_data/coins_date_and_values')
