import pandas as pd
import urllib.request
import json

token_names = ['public presale', 'public round', 'public sale', 'dao public sale',
               'sho', 'launchpad', 'public', 'public sale / sho', 'pre seed',
               'public round daomaker', 'idos, sho, early supporters', 'seed round',
               'seed sho', 'dao maker / platform raise sho', 'public sale price',
               'private round (including seed sho)', 'public sho', 'public sale (sho)',
               'public round ido', 'sale', 'public round 2 (sho)', 'community offering (sho)',
               'public sale - sho']

exceptions_slugs = ['yin-finance', 'coinspaid', 'opulous', 'maki-swap', 'alphr', 'orao-network',
                    'plotx', 'definer', 'openpredict', 'orion-protocol', 'hubble', 'infinity-pad']

url ="https://api.daomaker.com/getCompanyWithOfferings?slug="
df = pd.read_csv("/Users/eaxes/DA Projects/CMC/data/collected_data/mined/price_token_test.csv", index_col = 0)

def load_json(slug):
    url_fetch = f"{url}{slug}"
    data = urllib.request.urlopen(url_fetch).read()
    return json.loads(data)

def get_schedule(token_json):
    print("***")
    str_result = ""
    if token_json["slug"] in exceptions_slugs:
        return "slug is in exception list \n"
    if 'vesting_data' in token_json:
        if 'tokenData' in token_json['vesting_data']:
            vesting_item = token_json['vesting_data']
            for item in token_json['vesting_data']['tokenData']:
                item_data = item
                if 'tokenDescription' in item and 'tokenName' in item:
                    if item['tokenName'].lower().strip() in token_names:
                        str_result += f"{item['tokenName']}:{item['tokenDescription']}\n"
        return str_result
    else:
        return 'no token description found'


slugs = df.slug.to_numpy()
print(slugs)
for item in slugs:
    print(item)
    json_item = load_json(item)
    print(get_schedule(json_item))

