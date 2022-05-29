import requests
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

with open("dao_maker.html") as file:
    src = file.read()

with open("gamium_metrics.html") as metrics_gamium_file:
    metrics = metrics_gamium_file.read()

# url = 'https://daomaker.com/'
# response = requests.get(url)
soup = BeautifulSoup(src, 'lxml')
soup_metrics = BeautifulSoup(metrics, "lxml")

company_names = []
some_data = soup.find_all("div", {"class": "company_single"})
for item in some_data:
    company_names.append(item.find("h4").text.strip())

ticker = soup_metrics.find("div", {"class": "metrics"}).find("h3").text

url = "https://daomaker.com/company/gamium"

r = requests.get(url)

html_soup = BeautifulSoup(r.content, 'html.parser')
ticker_url = html_soup.find("div", {"class": "div.tabs_screening"})
print(ticker_url)

