import util_project.projects_names_parser
import util_project.json_parser
import util_project.json_parser_bs4
import util_project.transformer
from API.coingecko import coingecko_api
import json
import urllib.request
import pandas as pd
from classes.Project import Project
result = []
page = 1
test_unit = util_project.json_parser_bs4.get_json_funded_companies_page(page)

while len(test_unit) != 0:
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
    slug = project["slug"]
    coingecko_id = project["coingecko_id"]

    print(f"Name: {name}")
    print(f"Goingecko ID: {coingecko_id}")
    print(f"Slug: {slug}")
    print(f"Ticker: {ticker}")
    print(f"Personal allocation: {personal_allocation}")
    print("***")


