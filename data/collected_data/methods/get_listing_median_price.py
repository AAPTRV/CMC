import pandas as pd
import datetime


path_to_values = '/Users/eaxes/DA Projects/CMC/data/collected_data/coins_date_and_values'


def coin_id_list_to_median_price(list_item, hours):
    result_list = []
    for item_id in list_item:
        result_list.append(get_listing_sell_price(hours, path_to_values, item_id))
    return result_list


def get_listing_sell_price(hours, path_to_values, coingecko_id):
    print('Listing sell price processing ...')
    try:
        id = int(coingecko_id)
        dateparse = lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M')
        df_values = pd.read_csv(path_to_values, index_col=0,
                                parse_dates=['date'],
                                date_parser=dateparse)
        df_values_for_coin = df_values.query('coingecko_numerical_id == @id')
        if df_values_for_coin.empty:
            return 'no-price'
        else:
            border_date = df_values_for_coin.date.min() + datetime.timedelta(hours=hours)
            df_border_values = df_values_for_coin.query("date < @border_date")
            return df_border_values.value.median()
    except BaseException:
        return 'no-price'



