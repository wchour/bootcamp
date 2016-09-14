import random

import numpy as np

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# # The following is specific Jupyter notebooks
# %matplotlib inline
# %config InlineBackend.figure_formats = {'png', 'retina'}

x = np.random.random(size=100000)

def ecdf(data):
    return np.sort(data),np.arange(1, len(data)+1)/len(data)

x_ecdf, y_ecdf = ecdf(x)

plt.plot(x_ecdf[::1000], y_ecdf[::1000], marker='.', linestyle='none', markersize=10)

# Generating random #s to calculate probability of coin flip.

x = np.random.random(size=20)
heads = x <= 0.5
np.sum(heads)

x = np.random.random(size=36)
reversals = x <= 9/36
np.sum(reversals)

np.random.normal(7, 1, size=10)

x = np.random.normal(7, 1, size=10000)
plt.hist(x, bins=100)

np.random.randint(0, 4, size=20)

# Generate random sequence of bases
bases = 'ATGC'
x = np.random.randint(0, 4, size=50)

seq_list = [None]*50

for i, b in enumerate(x):
    seq_list[i] = bases[b]

''.join(seq_list)

# Generate 20 random values from 0-96.
np.random.randint(0,96,20)

# Generate 20 random values from 0-96, without repeats.
np.random.choice(np.arange(96), size=20, replace=False)

# Generate permutation.
np.arange(52)
np.random.permutation(np.arange(52))
