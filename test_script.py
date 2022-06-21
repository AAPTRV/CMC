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

# day = 86400, month =
day = "d"
week = "w"
month = "m"
schedule = {
    "20% at TGE, 90 days cliff then linear vesting for 12 months": [["0", 0.2],
                                                                    [f"4{month}", 0.066],  # linear vesting (1)
                                                                    [f"1{month}", 0.066],  # linear vesting (2)
                                                                    [f"1{month}", 0.066],  # linear vesting (3)
                                                                    [f"1{month}", 0.066],  # linear vesting (4)
                                                                    [f"1{month}", 0.066],  # linear vesting (5)
                                                                    [f"1{month}", 0.066],  # linear vesting (6)
                                                                    [f"1{month}", 0.066],  # linear vesting (7)
                                                                    [f"1{month}", 0.066],  # linear vesting (8)
                                                                    [f"1{month}", 0.066],  # linear vesting (9)
                                                                    [f"1{month}", 0.066],  # linear vesting (10)
                                                                    [f"1{month}", 0.066],  # linear vesting (11)
                                                                    [f"1{month}", 0.066]],  # linear vesting (12)

    "50% at TGE, 60 days cliff then 5% monthly":                   [["0", 0.2],
                                                                    [f"4{month}", 0.066],  # linear vesting (1)
                                                                    [f"1{month}", 0.066],  # linear vesting (2)
                                                                    [f"1{month}", 0.066],  # linear vesting (3)
                                                                    [f"1{month}", 0.066],  # linear vesting (4)
                                                                    [f"1{month}", 0.066],  # linear vesting (5)
                                                                    [f"1{month}", 0.066],  # linear vesting (6)
                                                                    [f"1{month}", 0.066],  # linear vesting (7)
                                                                    [f"1{month}", 0.066],  # linear vesting (8)
                                                                    [f"1{month}", 0.066],  # linear vesting (9)
                                                                    [f"1{month}", 0.066],  # linear vesting (10)
                                                                    [f"1{month}", 0.066],  # linear vesting (11)
                                                                    [f"1{month}", 0.066]],  # linear vesting (12)
}

url = "https://api.daomaker.com/getCompanyWithOfferings?slug="
df = pd.read_csv("/Users/eaxes/DA Projects/CMC/data/collected_data/mined/price_token_test.csv", index_col=0)


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
