import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load the food data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

# Make the bin boundaries.

bins = np.arange(1700, 2500, 50)

# Plot the data as a histogram
_ = plt.hist(xa_low, bins=bins)
plt.xlabel('Cross-sectional area(μm$^2$)')
plt.ylabel('count')
plt.show()
