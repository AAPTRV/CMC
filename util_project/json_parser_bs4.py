from bs4 import BeautifulSoup
import requests


def get_json(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup.find("script", {"id": "com.daomaker.daopad-state"}).text
