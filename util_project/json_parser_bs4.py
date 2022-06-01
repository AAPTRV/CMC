import time

from bs4 import BeautifulSoup
import requests


def get_json(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    result = soup.find("script", {"type": "application/json"})
    if isinstance(result, None):
        return "None type result while parsing ... "
    return result.text


#result = soup.find("script", {"id": "com.daomaker.daopad-state"})