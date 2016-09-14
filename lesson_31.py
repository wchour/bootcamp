import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Load the data
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# Take a look
df

# Slice out big forces (two different ways!)
df_big_force = df[df['impact force (mN)'] > 1000]

df_big_force = df.loc[df['impact force (mN)'] > 1000, :]

# Look at it
df_big_force

df.loc[(df['date']=='2013_05_27') & (df['trial number']==3) & (df['ID']=='III'),:]
df.loc[:,['impact force (mN)', 'adhesive force (mN)']]

# Only reveal impact force and adhesive force of frog I.
df.loc[(df['ID']=='I'),['impact force (mN)', 'adhesive force (mN)']]

plt.plot(df['impact force (mN)'], df['adhesive force (mN)'], marker='.',
         linestyle='none')
plt.xlabel('impact force (mN)')
plt.ylabel('adhesive force (mN)')

plt.plot(df.loc[:,'total contact area (mm2)'], df['adhesive force (mN)'], marker='.',
         linestyle='none')

df.plot(x='total contact area (mm2)', y='adhesive force (mN)', kind='scatter')

# Obtain correlation coefficient pairs across all variables.
df.corr()

# Rename the impact force column
df = df.rename(columns={'impact force (mN)': 'impf'})

# Short way to express impact force values.
df.impf
df.loc[:,['impact force (mN)']]
