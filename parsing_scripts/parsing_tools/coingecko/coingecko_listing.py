import json
import cloudscraper
import pandas as pd
from datetime import datetime

url_test = 'https://www.coingecko.com/price_charts/13915/usd/max.json'
scraper = cloudscraper.create_scraper()


def get_coin_chart(coingecko_id):
    page_text = scraper.get(f'https://www.coingecko.com/price_charts/{coingecko_id}/usd/max.json').text
    return json.loads(page_text)


def get_coin_chart_dataframe(coingecko_numerical_id):
    df_chart = pd.DataFrame(columns=['coingecko_numerical_id', 'date', 'value'])
    dict = get_coin_chart(coingecko_numerical_id)
    for item in dict['stats']:
        item_date = datetime.utcfromtimestamp(item[0] / 1000).strftime('%Y-%m-%d %H:%M')
        item_series = pd.Series({'coingecko_numerical_id':coingecko_numerical_id, 'date': item_date, 'value': item[1]})
        df_chart = df_chart.append(item_series, ignore_index=True)
    return df_chart


def get_coin_chart_test():
    page_text = scraper.get(url_test).text
    return json.loads(page_text)
