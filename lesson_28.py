import numpy as np

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Function to replicate data set N times, and for each time, compute a desired
# function, returning the array of computed replicates.

def draw_bs_reps(data, func, size=1):

    n_reps = 100
    replicates = np.empty(n_reps)
    for i in range(n_reps):
        sample = np.random.choice(data, replace=True, size=len(data))
        replicates[i] = func(sample)
    return replicates

def conf_int(replicates):
    # Compute confidence interval
    conf_int = np.percentile(replicates, [2.5, 97.5])
    print(conf_int)


bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')

def ecdf(data):
    return np.sort(data),np.arange(1, len(data)+1)/len(data)

x_1975, y_1975 = ecdf(bd_1975)

# plt.plot(x_1975, y_1975, marker='.', linestyle='none', color='blue')

n_reps = 100
for i in range(n_reps):
    x = np.random.choice(bd_1975, len(bd_1975))
    xr_1975, yr_1975 = ecdf(x)
    plt.plot(xr_1975, yr_1975, marker='.', linestyle='none', color='blue', alpha=0.01)
    plt.margins(0.02)
