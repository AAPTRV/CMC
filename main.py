import requests
from bs4 import BeautifulSoup

with open("dao_maker.html") as file:
    src = file.read()

# url = 'https://daomaker.com/'
# response = requests.get(url)
soup = BeautifulSoup(src, 'lxml')

company_names = []
some_data = soup.find_all("div", {"class": "company_single"})
for item in some_data:
    company_names.append(item.find("h4").text.strip())


print(company_names)