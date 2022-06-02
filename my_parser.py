import parsing_scripts.parsing_tools.daomaker.json_parser_bs4
import util_project.transformer
import parsing_scripts.parsing_tools.coingecko.coingecko_parsing as cg

result = []
page = 1
test_unit = parsing_scripts.parsing_tools.daomaker.json_parser_bs4.get_json_funded_companies_page(page)

while len(test_unit) != 0:

    for project in test_unit:
        slug_json = parsing_scripts.parsing_tools.daomaker.json_parser_bs4.get_json_from_slug(project["slug"])
        print(slug_json["data_table1"])
        company_dict = util_project.transformer.transform_slug_json_into_dict(slug_json)
        result.append(company_dict)

    print("**************\n")
    page += 1
    test_unit = parsing_scripts.parsing_tools.daomaker.json_parser_bs4.get_json_funded_companies_page(page)

print("---------------------------------")

for project in result:
    ticker = project["ticker"]
    name = project["name"]
    personal_allocation = project["personal_allocation"]
    slug = project["slug"]
    coingecko_id = project["coingecko_id"]
    if type(coingecko_id) is None:
        coingecko_id = 'default'
    coingecko_id_numerical = 'default'

    if coingecko_id != "default" and type(coingecko_id) is not None:
        coingecko_id_numerical = cg.get_token_numerical_id(coingecko_id)

    print(f"Name: {name}")
    print(f"Goingecko ID: {coingecko_id}")
    print(f"Coingecko numerical ID: {coingecko_id_numerical}")
    print(f"Slug: {slug}")
    print(f"Ticker: {ticker}")
    print(f"Personal allocation: {personal_allocation}")

    print("***")


