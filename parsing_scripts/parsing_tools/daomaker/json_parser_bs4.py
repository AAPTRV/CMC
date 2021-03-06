from bs4 import BeautifulSoup
import requests
import urllib.request
import json
import re
import pandas as pd
import numpy as np


def get_token_presale_price(slug):
    url = f'https://api.daomaker.com/getCompanyWithOfferings?slug={slug}'
    data = urllib.request.urlopen(url).read()
    json_gathered = json.loads(data)
    if isinstance(json_gathered, type(None)):
        return "default"
    if "public_sale_price" in json_gathered:
        result = json_gathered['public_sale_price']
        return result
    else:
        return "default"


def get_token_personal_cap(slug):
    url = f'https://api.daomaker.com/getCompanyWithOfferings?slug={slug}'
    data = urllib.request.urlopen(url).read()
    json_gathered = json.loads(data)
    result = "default"
    if isinstance(json_gathered, type(None)):
        return "default"
    if "offerings" in json_gathered:
        if len(json_gathered['offerings']) != 0:
            result = json_gathered['offerings'][0]['personal_cap']
            return result
        else:
            return result
    else:
        return result



def get_json(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    result = soup.find("script", {"type": "application/json"})
    if isinstance(result, type(None)):
        return "None type result while parsing_tools ... "
    return result.text


def get_json_funded_companies_page(page_number):
    url = f"https://api.daomaker.com/getFundedCompanies?page={page_number}"
    data = urllib.request.urlopen(url).read()
    return json.loads(data)


def get_json_from_slug (slug):
    url = f"https://api.daomaker.com/getCompanyWithOfferings?slug={slug}"
    data = urllib.request.urlopen(url).read()
    return json.loads(data)



