import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Write a function, backtrack_steps(), that computes the number of steps it
# takes for a random walker (i.e., polymerase) starting at position  x=0 to get
# to position  x=+1. It should return the number of steps to take the walk.

def backtrack_steps():
    #probability is probability of backtrack
    p = 0.5
    steps = 0
    forward = False
    while forward == False:
        x = np.random.random(1)
        steps += 1
        if x > p:
            forward = True
    return steps

# Generate 10,000 of these backtracks in order to get enough samples out of  P(tbt).
# (If you are interested in a way to really speed up this calculation, ask me about Numba.)

def manysteps():
    n = 10000
    x = [0]*n
    for i in range(n):
        x[i] = backtrack_steps()
    return x

# Use plt.hist() to plot a histogram of the backtrack times. Use the normed=True
# kwarg so it approximates a probability distribution function.
