import util_project.projects_names_parser
import util_project.json_parser
import util_project.json_parser_bs4
import util_project.transformer
from API.coingecko import coingecko_api
import json
import urllib.request
import pandas as pd
from classes.Project import Project

# url = "https://daomaker.com/"
# our_list = util_project.projects_names_parser.get_projects_as_objects(url)
#
# df = pd.DataFrame(columns=['name', 'ticket', 'url'])
#
# for project in our_list:
#     df = df.append(project.get_series(), ignore_index=True)
#
# print(df.shape)
# print(df)
result = []
page = 1
test_unit = util_project.json_parser_bs4.get_json_funded_companies_page(page)

while page == 1:
# while len(test_unit) == 10:
    print(f"PARSING NUMBER {page}")

    for project in test_unit:
        slug_json = util_project.json_parser_bs4.get_json_from_slug(project["slug"])
        print(slug_json["data_table1"])
        company_dict = util_project.transformer.transform_slug_json_into_dict(slug_json)
        result.append(company_dict)

    print("**************\n")
    page += 1
    test_unit = util_project.json_parser_bs4.get_json_funded_companies_page(page)

print("---------------------------------")

for project in result:
    ticker = project["ticker"]
    name = project["name"]
    personal_allocation = project["personal_allocation"]

    print(f"Ticker: {ticker}")
    print(f"Name: {name}")
    print(f"Personal allocation: {personal_allocation}")
    print("***")


