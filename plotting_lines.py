import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns

# Generate an array of x values.
x = np.linspace(-15, 15, 400)

# Compute the normalized intensity
plt.close()
norm_I = 4 * (scipy.special.j1(x) / x)**2
plt.plot(x, norm_I, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('$x$')
plt.ylabel('$I(x)/I_0$')

# Processing the spike data.
data = np.loadtxt('data/retina_spikes.csv', comments='#', skiprows=2, delimiter=',' )
t = data[:,0]
V = data[:,1]

# Close all other plots just in case.
plt.close()
plt.plot(t, V)
plt.xlabel('t (ms)')
plt.ylabel('V (μV)')
plt.xlim(1395, 1400)
