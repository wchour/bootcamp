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
