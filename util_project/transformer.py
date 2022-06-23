import parsing_scripts.parsing_tools.daomaker.json_parser_bs4 as js
import re
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

CONST_TICKERS = ['Ticker:', 'Ticker', 'Key MetricsTicker']
CONST_ALLOCATIONS = ["Personal Allocation:", "Individual Allocation:",
                     "Individual Allocation: ", "DAO SHO Individual Allocation:",
                     "DAO SHO Personal Allocation: ", "Allocation:", "Personal Allocation (Round 2):",
                     "Hardcap (SHO):", "Personal Cap (SHO)"]

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

def get_url_from_project_name(name, base_url):
    #TODO write in RegEx
    result = name.replace(" ", "-").replace(".", "-")
    return base_url + f"{result}"


def get_schedule(token_json):
    print("***")
    if "slug" in token_json:
        print(token_json["slug"])
    else:
        print('no-slug')
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
                        print(f"{item['tokenName']}:{item['tokenDescription']}\n")
                        return f"{item['tokenName']}:{item['tokenDescription']}\n"
                    if item['tokenName'].lower().strip() in token_names_low_priority:
                        print(f"{item['tokenName']}:{item['tokenDescription']}\n")
                        return f"{item['tokenName']}:{item['tokenDescription']}\n"
        return 'no token description found'
    else:
        return 'no token description found'


def transform_slug_json_into_dict(json):

    name_default = "No name found through transform function"
    slug_default = "default"
    ticker_default = "No ticket found through transform function"
    personal_allocation_default = "No personal allocation found through transform function"
    coingecko_token_id = 'default'
    platform_raise_default = 'default'
    pre_listing_price_default = 'default'
    schedule_default = 'default'

    name = name_default
    slug = slug_default
    ticker = ticker_default
    personal_allocation = personal_allocation_default
    platform_raise = platform_raise_default
    pre_listing_price = pre_listing_price_default
    schedule = schedule_default
    schedule = get_schedule(json)

    if "platform_raise" in json:
        platform_raise = json["platform_raise"]
    if "title" in json:
        name = json["title"]
    if "slug" in json:
        slug = json["slug"]
    if slug != 'default':
        personal_allocation = js.get_token_personal_cap(slug)
    if "coingecko_tokenId" in json:
        coingecko_token_id = json["coingecko_tokenId"]
        if coingecko_token_id is None:
            coingecko_token_id = 'default'

    if "offerings" in json:
        if len(json["offerings"]) != 0:
            pre_listing_price = json["offerings"][0]["price_per_token"]
        else:
            if slug != "default":
                pre_listing_price = js.get_token_presale_price(slug)

    for table in json['data_table1']:

        if ticker == ticker_default:
            for item in CONST_TICKERS:
                if item in table.values():
                    ticker = table["value"]
                    break


    return {'ticker': ticker,
            'name': name,
            'personal_allocation': personal_allocation,
            'slug': slug,
            'platform_raise': platform_raise,
            'coingecko_id': coingecko_token_id,
            'pre_listing_price': pre_listing_price,
            'schedule': schedule}

