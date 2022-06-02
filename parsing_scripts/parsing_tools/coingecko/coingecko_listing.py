import json
import cloudscraper

url_test = 'https://www.coingecko.com/price_charts/13915/usd/max.json'
scraper = cloudscraper.create_scraper()


def get_coin_chart(coingecko_id):
    page_text = scraper.get(f'https://www.coingecko.com/price_charts/{coingecko_id}/usd/max.json').text
    return json.loads(page_text)


def get_coin_chart_test():
    page_text = scraper.get(url_test).text
    return json.loads(page_text)
