import json
import urllib.request
import pandas as pd


def get_coin_list():
    data = urllib.request.urlopen("https://api.coingecko.com/api/v3/coins/list").read()
    return json.loads(data)
