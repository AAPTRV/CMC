import util_project.projects_names_parser
import util_project.json_parser
import util_project.json_parser_bs4
from API.coingecko import coingecko_api
import json
import urllib.request
import pandas as pd
from classes.Project import Project

url = "https://daomaker.com/"
our_list = util_project.projects_names_parser.get_projects_as_objects(url)

df = pd.DataFrame(columns=['name', 'ticket', 'url'])

for project in our_list:
    df = df.append(project.get_series(), ignore_index=True)

print(df.shape)


# test_unit = util_project.json_parser_bs4.get_json("https://daomaker.com/company/bbs-network")
# print(test_unit)