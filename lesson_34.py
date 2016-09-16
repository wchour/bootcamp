import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Load the data
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# Rename impact force column
df = df.rename(columns={'impact force (mN)': 'impf'})

# Mean impact force of frog I
np.mean(df.loc[df['ID']=='I', 'impf'])

# Mean impact force of each frog via for loop
mean_impf = np.empty(4)
sem_impf = np.empty(4)
for i, frog in enumerate(['I', 'II', 'III', 'IV']):
    mean_impf[i] = np.mean(df.loc[df['ID']==frog, 'impf'])
    n = np.sum(df['ID']=='I')
    sem_impf[i] = np.std(df.loc[df['ID']==frog, 'impf']) / np.sqrt(n)

print(mean_impf)
print(sem_impf)

# Mean impact force of each frog via groupby method
gb_frog = df.groupby('ID')
mean_impf = gb_frog['impf'].mean()
sem_impf = gb_frog['impf'].sem()

print(mean_impf)
print(sem_impf)

# Bar graph w/ error bars.
plt.bar(np.arange(4), mean_impf, yerr=sem_impf, ecolor='black',
        tick_label=['I', 'II', 'III', 'IV'], align='center')
plt.ylabel('impact force (mN)')

# Bar graph w/ erro bars using Seaborn.
sns.barplot(data=df, x='ID', y='impf')
plt.xlabel('')
plt.ylabel('impact force (mN)')

# Plot swarm plot instead
sns.swarmplot(data=df, x='ID', y='impf')
plt.margins(0.02)
plt.xlabel('')
plt.ylabel('impact force (mN)')

# Add hue colors to highlight individual dates of measurement.
ax = sns.swarmplot(data=df, x='ID', y='impf', hue='date')
ax.legend_.remove()
plt.margins(0.02)
plt.xlabel('')
plt.ylabel('impact force (mN)')
plt.gca().legend_.remove()

# If too many data points, use box plot instead of swarm plot.
sns.boxplot(data=df, x='ID', y='impf')
plt.margins(0.02)
plt.xlabel('')
plt.ylabel('impact force (mN)')
