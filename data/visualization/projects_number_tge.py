import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/eaxes/DA Projects/CMC/data/collected_data/coins_date_and_values')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%dT%H:%M:').dt.strftime('%Y-%m')

df_tge = df.groupby(['coingecko_numerical_id']).agg({"date":"min"}).reset_index()
df_tge = df_tge.groupby(['date']).agg({'coingecko_numerical_id':'count'})

sns.set(rc={'figure.figsize': (15, 10)},
        style="whitegrid", font_scale= 0.8)
sns.lineplot(data=df_tge, x="date", y="coingecko_numerical_id")
plt.legend(title='DAO MAKER TGE of projects per month', loc='upper left')
plt.show()
