import pandas as pd
import numpy as np
from datetime import date
import time
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import re
from time import gmtime, strftime
import data.collected_data.economics.schedule as sch

sns.set(rc={'figure.figsize': (15, 10)},
        style="whitegrid", font_scale= 0.8)

token_names = ['public presale', 'public round', 'public sale', 'dao public sale',
               'sho', 'launchpad', 'public', 'public sale / sho',
               'public round daomaker', 'idos, sho, early supporters',
               'seed sho', 'dao maker / platform raise sho', 'public sale price',
               'private round (including seed sho)', 'public sho', 'public sale (sho)',
               'public round ido', 'sale', 'public round 2 (sho)', 'community offering (sho)',
               'public sale - sho']

token_names_low_priority = ['pre seed', 'seed round']

exceptions_slugs = ['yin-finance', 'coinspaid', 'opulous', 'maki-swap', 'alphr', 'orao-network',
                    'plotx', 'definer', 'openpredict', 'orion-protocol', 'hubble', 'infinity-pad']

path_to_values = '/Users/eaxes/DA Projects/CMC/data/collected_data/coins_date_and_values'
base_df_path = "/Users/eaxes/DA Projects/CMC/data/collected_data/mined/price_token_test.csv"
values_df_path = '/Users/eaxes/DA Projects/CMC/data/collected_data/coins_date_and_values'

def get_schedule(token_json):
    print("***")
    str_result = ""
    if token_json["slug"] in exceptions_slugs:
        return "slug is in exception list \n"
    if 'vesting_data' in token_json:
        if 'tokenData' in token_json['vesting_data']:
            vesting_item = token_json['vesting_data']
            for item in token_json['vesting_data']['tokenData']:
                item_data = item
                if 'tokenDescription' in item and 'tokenName' in item:
                    if item['tokenName'].lower().strip() in token_names:
                        return f"{item['tokenName']}:{item['tokenDescription']}\n"
                    if item['tokenName'].lower().strip() in token_names_low_priority:
                        return f"{item['tokenName']}:{item['tokenDescription']}\n"
        return 'no token description found'
    else:
        return 'no token description found'


def get_median_price_at_date(hours, path_to_values, coingecko_id, date64):
    dateparse = lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M')
    df_values = pd.read_csv(path_to_values, index_col=0,
                            parse_dates=['date'],
                            date_parser=dateparse)
    df_values = df_values.query("coingecko_numerical_id == @coingecko_id")
    border_right = date64 + np.timedelta64(hours, 'h')
    df_values = df_values.query("date < @border_right and date > @date64")
    return df_values.value.median()


def str_schedule_unit_to_arr(schedule):
    time = re.findall("[a-z]+", schedule)[0]
    quantity = re.findall("\d+", schedule)[0]
    return [quantity, time]


def get_tge_date(path_to_values, coingecko_id):
    print('Tge date processing...')
    try:
        id = int(coingecko_id)
        dateparse = lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M')
        df_values = pd.read_csv(path_to_values, index_col=0,
                                parse_dates=['date'],
                                date_parser=dateparse)
        df_values_for_coin = df_values.query('coingecko_numerical_id == @id')
        if df_values_for_coin.empty:
            return 'no-date'
        else:
            return df_values_for_coin.date.min()
    except BaseException:
        return 'base-exception'

def get_token_eco_df(slug, coingecko_numerical_id):
    slug = "gamefi"
    coingecko_numerical_id = 18292
    df = pd.read_csv(base_df_path, index_col=0)
    token_common_df = df.query("slug == @slug")
    token_charts = pd.read_csv(values_df_path, index_col=0).query('coingecko_numerical_id == @coingecko_numerical_id')
    schedule_table = sch.schedule
    schedule = "Public:25% at TGE, then 25% at month 2, 4, and 6"
    personal_cap = float(token_common_df.token_personal_cap.values[0])
    table = schedule_table[schedule]

    result_df = pd.DataFrame(columns=['token_numerical_id', 'sale_date',
                                      'tokens_for_sale', 'median_price', 'profit'])
    result = []
    tge_date = get_tge_date(path_to_values, coingecko_numerical_id)
    for i in range(len(table)):
        if table[i][0] == "0":
            result.append([tge_date, personal_cap * float(table[i][1])])
        else:
            schedule = str_schedule_unit_to_arr(table[i][0])
            previous_date = result[i - 1][0]
            current_date = previous_date + np.timedelta64(int(schedule[0]), 'M')
            if current_date > pd.Timestamp(datetime.datetime.now()) + np.timedelta64(48, 'h'):
                break
            result.append([current_date, personal_cap * float(table[i][1])])

    eco = []

    for stack in result:
        median_price = get_median_price_at_date(48, path_to_values, 18292, stack[0])
        eco.append([stack[0], stack[1] * median_price])
        d = {'a': 1, 'b': 2, 'c': 3}
        ser = pd.Series(data=d, index=['a', 'b', 'c'])
        series = pd.Series({'token_numerical_id': coingecko_numerical_id,
                            'sale_date': stack[0],
                            'tokens_for_sale': stack[1],
                            'median_price': get_median_price_at_date(48, path_to_values, 18292, stack[0]),
                            'profit': stack[1] * get_median_price_at_date(48, path_to_values, 18292, stack[0])
                            })
        result_df = result_df.append(series, ignore_index=True)
    return result_df

print(get_token_eco_df(123,123))

