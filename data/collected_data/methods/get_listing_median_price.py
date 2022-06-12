import pandas as pd
import datetime


def get_listing_sell_price(hours, path_to_values, coingecko_id):
    dateparse = lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M')
    df_values = pd.read_csv(path_to_values, index_col=0,
                            parse_dates=['date'],
                            date_parser=dateparse)
    df_values_for_coin = df_values.query('coingecko_numerical_id == @coingecko_id')
    border_date = df_values_for_coin.date.min() + datetime.timedelta(hours=hours)
    df_border_values = df_values_for_coin.query("date < @border_date")
    return df_border_values.value.median()
