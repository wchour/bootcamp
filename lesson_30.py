import numpy as np

# Pandas, conventionally imported as pd
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Read in data files with pandas
df_high = pd.read_csv('data/xa_high_food.csv', comment='#', header=None)
df_low = pd.read_csv('data/xa_low_food.csv', comment='#', header=None)

# Dictionary of top men's World Cup scorers and how many goals
wc_dict = {'Klose': 16,
           'Ronaldo': 15,
           'Müller': 14,
           'Fontaine': 13,
           'Pelé': 12,
           'Koscis': 11,
           'Klinsmann': 11}

# Create a Series from the dictionary
s_goals = pd.Series(wc_dict)

# Take a look
s_goals

nation_dict = {'Klose': 'Germany',
           'Ronaldo': 'Brazil',
           'Müller': 'Germany',
           'Fontaine': 'France',
           'Pelé': 'Brazil',
           'Koscis': 'Hungary',
           'Klinsmann': 'Germany'}

s_nation = pd.Series(nation_dict)

df_wc = pd.DataFrame({'nation': s_nation, 'goals': s_goals})

# Change column headings
df_low.columns = ['low']
df_high.columns = ['high']

# Take a look
df_high

# Concatenate DataFrames
df = pd.concat((df_low, df_high), axis=1)

# See the result
df

# Write out DataFrame
df.to_csv('xa_combined.csv', index=False)

df_tidy = pd.melt(df, var_name='food density',
             value_name='cross-sectional area (sq micron)').dropna()

df_tidy.loc[(df_tidy['food density']=='low') & (df_tidy['cross-sectional area (sq micron)'] > 2100), :]
