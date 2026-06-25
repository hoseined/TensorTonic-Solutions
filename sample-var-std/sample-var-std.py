import numpy as np
from math import sqrt

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    n = len(x)
    x_bar = np.mean(x)
    sigma_res = np.pow(x - x_bar, 2)
    if n != 1:
        s2 = sigma_res.sum() / (n - 1)
    else:
        s2 = 0
    return s2, sqrt(s2)