import numpy as np

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Specify parameters
# Number of generations
n_gen = 16

# Chance of having beneficial mutation.
r = 1e-5

# Total number of cells
n_cells = 2**(n_gen - 1)

# Adaptive immunity: binomial distribution
# Draw 100000 binomial samples
ai_samples = np.random.binomial(n_cells, r, 100000)

counts = np.bincount(ai_samples)
plt.plot(np.arange(len(counts)), counts, marker='.', linestyle='none')

print('AI mean: ', np.mean(ai_samples))
print('AI std: ', np.std(ai_samples))
print('AI Fano: ', np.var(ai_samples)/np.mean(ai_samples))

# Plot histogram, but it's a probability mass function, so no need for bins
plt.plot(np.bincount(ai_samples) / len(ai_samples), marker='.', markersize=10,
        linestyle='None')

plt.xlabel('Number of survivors')
plt.ylabel('Probability')
plt.xticks(np.arange(ai_samples.max()+1));
plt.margins(0.02)

# Function to draw out of random mutation hypothesis
def draw_random_mutation(n_gen, r):
    """Draw a sample out of the Luria-Delbruck distribution"""
    # Initialize number of mutants
    n_mut = 0

    for g in range(n_gen):
        n_mut = 2 * n_mut + np.random.binomial(2**g - 2 * n_mut, r)

    return n_mut

def sample_random_mutation(n_gen, r, size=1):
    """Sample out of the Luria-Delbruck distribution"""
    # Initialize samples
    samples = np.empty(size)

    # Draw the samples
    for i in range(size):
        samples[i] = draw_random_mutation(n_gen, r)

    return samples

rm_samples = sample_random_mutation(n_gen, r, size=100000)
x_ai, y_ai = ecdf(ai_samples)
x_rm, y_rm = ecdf(rm_samples)

plt.plot(x_ai, y_ai)
plt.clf()
plt.plot(x_ai, y_ai)
plt.clf()
plt.plot(x_ai, y_ai, marker='.', linestyle='none')
plt.plot(x_rm, y_rm, marker='.', linestyle='none')
plt.xscale('log')
