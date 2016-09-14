import numpy as np

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))


def ecdf(data):
    return np.sort(data),np.arange(1, len(data)+1)/len(data)

# Compute ECDFs for 1975 and 2012
x_1975, y_1975 = ecdf(bd_1975)
x_2012, y_2012 = ecdf(bd_2012)
x_1975_bs, y_1975_bs = ecdf(bs_sample)

# # Plot the ECDFs
# plt.plot(x_1975, y_1975, marker='.', linestyle='none')
# plt.plot(x_2012, y_2012, marker='.', linestyle='none')
# plt.margins(0.02)
# plt.xlabel('beak depth (mm)')
# plt.ylabel('ECDF')
# plt.legend(('1975', '2012'), loc='lower right')
#
# np.mean(bd_1975), np.mean(bd_2012)
#
# len(bd_1975), len(bd_2012)

# Plot the ECDFs
plt.plot(x_1975, y_1975, marker='.', linestyle='none')
plt.plot(x_1975_bs, y_1975_bs, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('beak depth (mm)')
plt.ylabel('ECDF')
plt.legend(('1975', 'bs'), loc='lower right')

np.mean(bd_1975), np.mean(bd_2012), np.mean(bs_sample)

len(bd_1975), len(bd_2012)

bs_replicate = np.mean(bs_sample)
bs_replicate

# Number of replicas
n_reps = 100000

# Initialize bootstrap replicas array
bs_replicates_1975 = np.empty(n_reps)

# Compute replicates
for i in range(n_reps):
    bs_sample = np.random.choice(bd_1975, size=len(bd_1975))
    bs_replicates_1975[i] = np.mean(bs_sample)

# Plot histogram of replicates
_ = plt.hist(bs_replicates_1975, bins=100, normed=True)
plt.xlabel('mean beak depth (mm)')
plt.ylabel('PDF')

# Compute 95% confidence interval.
conf_int_1975 = np.percentile(bs_replicates_1975, [2.5, 97.5])
conf_int_1975



# Do the same for 2012 data.
# Number of replicas
n_reps = 100000

# Initialize bootstrap replicas array
bs_replicates_2012 = np.empty(n_reps)

# Compute replicates
for i in range(n_reps):
    bs_sample = np.random.choice(bd_2012, size=len(bd_2012))
    bs_replicates_2012[i] = np.mean(bs_sample)

# Compute the confidence interval
conf_int_2012 = np.percentile(bs_replicates_2012, [2.5, 97.5])

_ = plt.hist(bs_replicates_2012, bins=100, normed=True)
plt.xlabel('mean beak depth (mm)')
plt.ylabel('PDF')

print(conf_int_1975)
print(conf_int_2012)

# Now compute std dev, for actual data and replicates of 1975 data.

bs_sem = np.std(bs_replicates_1975)
bs_sem

sem = np.std(bd_1975, ddof=1) / np.sqrt(len(bd_1975))
sem


# Plot confidence interval of std dev bs_1975 replicates.

# Number of replicas
n_reps = 100000

# Initialize bootstrap replicas array
bs_replicates_1975 = np.empty(n_reps)

# Compute replicates
for i in range(n_reps):
    bs_sample = np.random.choice(bd_1975, size=len(bd_1975))
    bs_replicates_1975[i] = np.std(bs_sample)

# Compute confidence interval
conf_int_1975 = np.percentile(bs_replicates_1975, [2.5, 97.5])
print(conf_int_1975)

# Plot histogram
_ = plt.hist(bs_replicates_1975, bins=100, normed=True)
plt.xlabel('std. dev. beak depth (mm)')
plt.ylabel('PDF')
