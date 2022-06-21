import data.collected_data.methods.get_listing_median_price as gt
import parsing_scripts.parsing_tools.daomaker.json_parser_bs4 as js
import re

CONST_TICKERS = ['Ticker:', 'Ticker', 'Key MetricsTicker']
CONST_ALLOCATIONS = ["Personal Allocation:", "Individual Allocation:",
                     "Individual Allocation: ", "DAO SHO Individual Allocation:",
                     "DAO SHO Personal Allocation: ", "Allocation:", "Personal Allocation (Round 2):",
                     "Hardcap (SHO):", "Personal Cap (SHO)"]


def get_url_from_project_name(name, base_url):
    #TODO write in RegEx
    result = name.replace(" ", "-").replace(".", "-")
    return base_url + f"{result}"


def transform_slug_json_into_dict(json):

    name_default = "No name found through transform function"
    slug_default = "default"
    ticker_default = "No ticket found through transform function"
    personal_allocation_default = "No personal allocation found through transform function"
    coingecko_token_id = 'default'
    platform_raise_default = 'default'
    pre_listing_price_default = 'default'

    name = name_default
    slug = slug_default
    ticker = ticker_default
    personal_allocation = personal_allocation_default
    platform_raise = platform_raise_default
    pre_listing_price = pre_listing_price_default


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
            'pre_listing_price': pre_listing_price}

