import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Load the data
g1973 = pd.read_csv('data/grant_1973.csv', comment='#', header=0)
g1975 = pd.read_csv('data/grant_1975.csv', comment='#', header=0)
g1987 = pd.read_csv('data/grant_1987.csv', comment='#', header=0)
g1991 = pd.read_csv('data/grant_1991.csv', comment='#', header=0)
g2012 = pd.read_csv('data/grant_2012.csv', comment='#', header=0)

# First, change the name of the yearband column of the 1973 data to year.
# Also, make sure the year format is four digits, not two!
g1973 = g1973.rename(columns={'yearband':'year'})
g1973.loc[:, 'year'] = g1973['year'] + 1900


# Next, add a year column to the other four DataFrames. You want tidy data, so
# each row in the DataFrame should have an entry for the year.

a1975 = [1975]*len(g1975)
b1975 = pd.Series(a1975)
y1975 = pd.DataFrame({'year': b1975})
g1975 = pd.concat((g1975, y1975), axis=1)

a1987 = [1987]*len(g1987)
b1987 = pd.Series(a1987)
y1987 = pd.DataFrame({'year': b1987})
g1987 = pd.concat((g1987, y1987), axis=1)

a1991 = [1991]*len(g1991)
b1991 = pd.Series(a1991)
y1991 = pd.DataFrame({'year': b1991})
g1991 = pd.concat((g1991, y1991), axis=1)

a2012 = [2012]*len(g2012)
b2012 = pd.Series(a2012)
y2012 = pd.DataFrame({'year': b2012})
g2012 = pd.concat((g2012, y2012), axis=1)



# Change the column names so that all the DataFrames have the same column names.
# I would choose column names
# ['band', 'species', 'beak length (mm)', 'beak depth (mm)', 'year']

g1973 = g1973.rename(columns={'beak length':'beak length (mm)','beak depth':'beak depth (mm)'})
g1975 = g1975.rename(columns={'Beak length, mm':'beak length (mm)','Beak depth, mm':'beak depth (mm)'})
g1987 = g1987.rename(columns={'Beak length, mm':'beak length (mm)','Beak depth, mm':'beak depth (mm)'})
g1991 = g1991.rename(columns={'blength':'beak length (mm)', 'bdepth':'beak depth (mm)'})
g2012 = g2012.rename(columns={'blength':'beak length (mm)', 'bdepth':'beak depth (mm)'})

# Concatenate the DataFrames into a single DataFrame. Be careful with indices!
# If you use pd.concat(), you will need to use the ignore_index=True kwarg.
# You might also need to use the axis kwarg.
data = pd.concat((g1973, g1975, g1987, g1991, g2012), axis=0, ignore_index=True)

# After doing this work, it is worth saving your tidy DataFrame in a CSV document.
# To this using the to_csv() method of your DataFrame. Since the indices are
# uninformative, you should use the index=False kwarg. (I have already done this
# and saved it as ~/git/bootcamp/data/grant_complete.csv, which will help you do
# the rest of the exercise if you have problems with this part.)

pd.DataFrame.to_csv(data, 'data/beaks.csv')

# The band fields gives the number of the band on the bird's leg that was used to
# tag it. Are some birds counted twice? Are they counted twice in the same year?
# Do you think you should drop duplicate birds from the same year? How about
# different years? My opinion is that you should drop duplicate birds from the
# same year and keep the others, but I would be open to discussion on that. To
# practice your Pandas skills, though, let's delete only duplicate birds from the
# same year from the DataFrame. When you have made this DataFrame, save it as a
# CSV file.
# Hint: The DataFrame methods duplicated() and drop_duplicates() will be useful.

beaks = pd.read_csv('data/beaks.csv', comment='#', header=0)
x = beaks.drop_duplicates(subset =['band', 'year'])
pd.DataFrame.to_csv(x, 'data/beaks_clean.csv')


 # Plot an ECDF of beak depths of Geospiza fortis specimens measured in 1987.
 # Plot an ECDF of the beak depths of Geospiza scandens from the same year.
 # These ECDFs should be on the same plot. On another plot, plot ECDFs of beak
 # lengths for the two species in 1987. Do you see a striking phenotypic
 # difference?

def ecdf(data):
    return np.sort(data),np.arange(1, len(data)+1)/len(data)

x_fortis, y_fortis = ecdf(x.loc[(x['year'] == 1987) & (x['species'] == 'fortis'),
    ['beak depth (mm)']])
x_scandens, y_scandens = ecdf(x.loc[(x['year'] == 1987) & (x['species'] == 'scandens'),
    ['beak depth (mm)']])
plt.plot(x_fortis, y_fortis, marker='.', linestyle='none', color='blue', alpha=0.8)
plt.plot(x_scandens, y_scandens, marker='.', linestyle='none', color='green', alpha=0.8)
plt.margins(0.02)
plt.xlabel('Beak Depth (mm)')
plt.ylabel('Cumulative Probability')
plt.legend(('Geospiza fortis, 1987', 'Geospiza scandens, 1987'), loc='lower right')

x_fortis, y_fortis = ecdf(x.loc[(x['year'] == 1987) & (x['species'] == 'fortis'),
    ['beak length (mm)']])
x_scandens, y_scandens = ecdf(x.loc[(x['year'] == 1987) & (x['species'] == 'scandens'),
    ['beak length (mm)']])
plt.plot(x_fortis, y_fortis, marker='.', linestyle='none', color='blue', alpha=0.8)
plt.plot(x_scandens, y_scandens, marker='.', linestyle='none', color='green', alpha=0.8)
plt.margins(0.02)
plt.xlabel('Beak Length (mm)')
plt.ylabel('Cumulative Probability')
plt.legend(('Geospiza fortis, 1987', 'Geospiza scandens, 1987'), loc='lower right')




# e) Perhaps a more informative plot is to plot the measurement of each bird's beak
# as a point in the beak depth-beak length plane. For the 1987 data, plot beak depth
# vs. beak width for Geospiza fortis as blue dots, and for Geospiza scandens as red
# dots. Can you see the species demarcation?
d_fortis = x.loc[(x['year'] == 1987) & (x['species'] == 'fortis'),
    ['beak depth (mm)']]
w_fortis = x.loc[(x['year'] == 1987) & (x['species'] == 'fortis'),
    ['beak length (mm)']]
d_scandens = x.loc[(x['year'] == 1987) & (x['species'] == 'scandens'),
    ['beak depth (mm)']]
w_scandens = x.loc[(x['year'] == 1987) & (x['species'] == 'scandens'),
    ['beak length (mm)']]
plt.plot(w_fortis, d_fortis, marker='.', linestyle='none', color='blue', alpha=0.8)
plt.plot(w_scandens, d_scandens, marker='.', linestyle='none', color='red', alpha=0.8)


# f) Do part (e) again for all years. Describe what you see. Do you see the changes
# in the differences between species (presumably as a result of hybridization)?
# In your plots, make sure all plots have the same range on the axes.

def plot_stuff(year):
    d_fortis = x.loc[(x['year'] == year) & (x['species'] == 'fortis'),
        ['beak depth (mm)']]
    w_fortis = x.loc[(x['year'] == year) & (x['species'] == 'fortis'),
        ['beak length (mm)']]
    d_scandens = x.loc[(x['year'] == year) & (x['species'] == 'scandens'),
        ['beak depth (mm)']]
    w_scandens = x.loc[(x['year'] == year) & (x['species'] == 'scandens'),
        ['beak length (mm)']]
    plt.plot(w_fortis, d_fortis, marker='.', linestyle='none', color='blue', alpha=0.8)
    plt.plot(w_scandens, d_scandens, marker='.', linestyle='none', color='red', alpha=0.8)
    plt.margins(0.02)
    plt.xlabel('Beak Depth (mm)')
    plt.ylabel('Beak Width (mm)')
    plt.legend(('Geospiza fortis', 'Geospiza scandens'), loc='lower right')
    plt.title('Beak Depth vs Beak Width of Geospiza (' + str(year) + ')')
    plt.savefig('beaks_' + str(year) + '.pdf', bbox_inches='tight')
    plt.savefig('beaks_' + str(year) + '.svg', bbox_inches='tight')
    plt.close()

years = [1973, 1975, 1987, 1991, 2012]
for i in years:
    plot_stuff(i)
