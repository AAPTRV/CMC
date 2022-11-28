import urllib.request, json
url = "https://api.daomaker.com/getFundedCompaniesATH"
header= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '}

#the URL where you are requesting at
req = urllib.request.Request(url, headers=header)
page = urllib.request.urlopen(req).read()
print(page)