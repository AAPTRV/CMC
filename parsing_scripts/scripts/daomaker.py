import parsing_scripts.parsing_tools.daomaker.json_parser_bs4
import util_project.transformer
import parsing_scripts.parsing_tools.coingecko.coingecko_parsing as cg
import pandas as pd

url = 'https://daomaker.com/'


def get_data_from_dao():
    print('dao maker parsing script processing ...')

    df = pd.DataFrame(columns=['name', 'ticker', 'platform_raise','coingecko_id', 'coingecko_numerical_id'])
    page = 1
    result_of_parsing = []
    parser_unit = parsing_scripts.parsing_tools.daomaker.json_parser_bs4.get_json_funded_companies_page(page)

    while len(parser_unit) != 0:

        for project in parser_unit:
            print('dao maker parsing script processing ...')
            slug_json = parsing_scripts.parsing_tools.daomaker.json_parser_bs4.get_json_from_slug(project["slug"])
            company_dict = util_project.transformer.transform_slug_json_into_dict(slug_json)
            result_of_parsing.append(company_dict)

        page += 1
        parser_unit = parsing_scripts.parsing_tools.daomaker.json_parser_bs4.get_json_funded_companies_page(page)

    for project in result_of_parsing:
        print('dao maker parsing script processing ...')
        ticker = project["ticker"]
        name = project["name"]
        personal_allocation = project["personal_allocation"]
        slug = project["slug"]
        platform_raise = project["platform_raise"]
        coingecko_id = project["coingecko_id"]

        if type(coingecko_id) is None:
            coingecko_id = 'default'
        coingecko_id_numerical = 'default'

        if coingecko_id != "default" and type(coingecko_id) is not None:
            coingecko_id_numerical = cg.get_token_numerical_id(coingecko_id)

        s1 = pd.Series({'name': name,
                        'ticker': ticker,
                        'platform_raise': platform_raise,
                        'coingecko_id': coingecko_id,
                        'coingecko_numerical_id': coingecko_id_numerical})
        df = df.append(s1, ignore_index=True)

    return df

def get_data_from_dao_with_median():
    print('dao maker parsing script processing ...')

    df = pd.DataFrame(columns=['name', 'ticker', 'platform_raise','coingecko_id',
                               'coingecko_numerical_id', 'sho_price'])
    page = 1
    result_of_parsing = []
    parser_unit = parsing_scripts.parsing_tools.daomaker.json_parser_bs4.get_json_funded_companies_page(page)

    while len(parser_unit) != 0:

        for project in parser_unit:
            print('dao maker parsing script processing ...')
            slug_json = parsing_scripts.parsing_tools.daomaker.json_parser_bs4.get_json_from_slug(project["slug"])
            company_dict = util_project.transformer.transform_slug_json_into_dict(slug_json)
            result_of_parsing.append(company_dict)

        page += 1
        parser_unit = parsing_scripts.parsing_tools.daomaker.json_parser_bs4.get_json_funded_companies_page(page)

    for project in result_of_parsing:
        print('dao maker parsing script processing ...')
        ticker = project["ticker"]
        name = project["name"]
        personal_allocation = project["personal_allocation"]
        slug = project["slug"]
        platform_raise = project["platform_raise"]
        coingecko_id = project["coingecko_id"]
        sho_price = project["pre_listing_price"]
        print("at least one time that was correct")

        if type(coingecko_id) is None:
            coingecko_id = 'default'
        coingecko_id_numerical = 'default'

        if coingecko_id != "default" and type(coingecko_id) is not None:
            coingecko_id_numerical = cg.get_token_numerical_id(coingecko_id)

        s1 = pd.Series({'name': name,
                        'ticker': ticker,
                        'platform_raise': platform_raise,
                        'coingecko_id': coingecko_id,
                        'coingecko_numerical_id': coingecko_id_numerical,
                        'sho_price': sho_price})
        df = df.append(s1, ignore_index=True)

    return df

# get_data_from_dao().to_csv("/Users/eaxes/DA Projects/CMC/data/collected_data/mined/mined_table2.csv")
get_data_from_dao_with_median().to_csv("/Users/eaxes/DA Projects/CMC/data/collected_data/mined/price_token_test.csv")
