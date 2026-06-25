import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    x = np.array(x)

    if p > 1:
        raise ValueError(f'[Error] the value p: {p} can not be higher than 1')

    return ((p ** x) * (1 - p) ** (1 - x)), p, p * (1 - p)