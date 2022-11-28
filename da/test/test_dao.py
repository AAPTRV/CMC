import da.parsers.dao_parser as dp
import pandas as pd
import numpy as np

result = dp.get_json_with_companies_ath()
print(result)

df = pd.DataFrame(columns =
                  ['title', 'slug'])

for data in result:
    parsed_dict = {'title': data['title'], 'slug': data['slug']}
    parsed_df = pd.DataFrame(parsed_dict, index = [0])
    df = pd.concat([df, parsed_df], ignore_index=True)

df.to_csv('/Users/eaxes/DA Projects/CMC/da/test/dao_companies_ath_11')