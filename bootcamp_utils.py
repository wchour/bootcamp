import numpy as np

# bootcamp utils: a collection of statistical functions

def ecdf(data):
    '''
    Compute x, y values for an empirical distribution function.
    '''
    x = np.sort(data)
    y = np.arange(0, 1, 1/len(x))

    return x, y
