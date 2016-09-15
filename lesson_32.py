import numpy as np
import pandas as pd

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# Exercise 1

# Extract the impact time of all impacts that had an adhesive strength of
# magnitude greater than 2000 Pa.

df_impact = df.loc[(df['adhesive strength (Pa)'] < -2000), ['impact time (ms)']]

# Extract the impact force and adhesive force for all of Frog II's strikes.
df_II = df.loc[(df['ID']=='II'), ['impact force (mN)', 'adhesive force (mN)']]

# Extract the adhesive force and the time the frog pulls on the target for
# juvenile frogs (Frogs III and IV).
df_or = df.loc[(df['ID'] == 'III') | (df['ID'] == 'IV'), ['adhesive force (mN)', 'time frog pulls on target (ms)']]


# Exercise 2

# Extract all of Frog I's impact forces and compute the mean.
def mean_compute(ID):
    frog_if = df.loc[(df['ID'] == ID), ['impact force (mN)']]
    total = 0
    for i in range(len(frog_if)):
        total += frog_if.loc[i]
    return total/len(frog_if)

# Do the same for the other three frogs.
# Write a for loop to do this and return a NumPy array with the four mean impact forces.

# We only want ID's and impact forces, so slice those out
df_impf = df.loc[:, ['ID', 'impact force (mN)']]

# Make a GroupBy object
grouped = df_impf.groupby('ID')

# Apply the np.mean function to the grouped object
df_mean_impf = grouped.apply(np.mean)

# Look at the new DataFrame
df_mean_impf

# We can pull the mean impact force for a frog of interest using loc
df_mean_impf.loc['III', :]

# We can apply multiple functions to a GroupBy object using the agg() method.
# The argument of this method is a list of functions you want to apply.
grouped.agg([np.mean, np.median])


# Now, let's practice with groupby().
# a) Compute standard deviation of the impact forces for each frog.
df_std_impf = grouped.apply(np.std)

# b) Write a function, coeff_of_var(data), which computes the coefficient of
# variation of a data set. This is the standard deviation divided by the
# absolute value of the mean.

def coeff_of_var(data):
    df_std_impf = data.apply(np.std)
    df_mean_impf = data.apply(np.mean)
    df_abs_impf = df_mean_impf.apply(np.absolute)

    return df_std_impf/df_abs_impf

# c) Compute coefficient of variation of the impact forces and adhesive forces
# for each frog.

df_ifaf = df.loc[:, ['ID', 'impact force (mN)', 'adhesive force (mN)']]

def exer_c():
    df_ifaf = df.loc[:, ['ID', 'impact force (mN)', 'adhesive force (mN)']]
    grouped_ifaf = df_ifaf.groupby('ID')
    return coeff_of_var(grouped_ifaf)

# d) And now, finally.... Compute a DataFrame that has the mean, median,
# standard deviation, and coefficient of variation of the impact forces and
# adhesive forces for each frog.

def exer_d():
    df_ifaf = df.loc[:, ['ID', 'impact force (mN)', 'adhesive force (mN)']]
    df_ifaf = df_ifaf.groupby('ID')
    return df_ifaf.agg([np.mean, np.median, np.std])
