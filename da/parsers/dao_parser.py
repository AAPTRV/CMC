import urllib.request, json
url = "https://api.daomaker.com/getFundedCompaniesATH"
header= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '}


def get_json_with_companies_ath():
    req = urllib.request.Request(url, headers=header)
    page = urllib.request.urlopen(req).read()
    json_gathered = json.loads(page)
    if isinstance(json_gathered, type(None)):
        return "error while parsing ATH dao companies"
    else:
        return json_gathered