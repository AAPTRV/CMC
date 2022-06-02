from bs4 import BeautifulSoup
import cloudscraper

BASE_URL = "https://www.coingecko.com/en/coins/"
scraper = cloudscraper.create_scraper()


def get_token_numerical_id(slug_value):
    print(f'SLUG VALUE: {slug_value}')
    page_text = scraper.get(BASE_URL + slug_value).text
    soup = BeautifulSoup(page_text, "html.parser")
    result = soup.findAll('span', {"class": "no-wrap"})
    if len(result) > 0:
        return result[0]['data-coin-id']
    else:
        return 'no-id'

print(get_token_numerical_id('crowns'))