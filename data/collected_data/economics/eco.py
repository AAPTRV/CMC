import pandas as pd
import numpy as np

base_df_path = "/Users/eaxes/DA Projects/CMC/data/collected_data/mined/price_token_test.csv"

def get_eco_for_token(slug):
    df = pd.read_csv(base_df_path)
    token_df = df.query("slug == @slug")