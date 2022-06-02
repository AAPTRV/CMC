import pandas as pd
import numpy as np



df = pd.DataFrame(columns = ['name', 'ticket', 'coingecko_id', 'coingecko_numerical_id'])
s1 = pd.Series({'name': 'my_name', 'ticket': 'TCC', 'coingecko_id': '537', 'coingecko_numerical_id':'123'})
df = df.append(s1, ignore_index=True)

