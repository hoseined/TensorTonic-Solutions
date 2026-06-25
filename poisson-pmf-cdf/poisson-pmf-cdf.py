import numpy as np
import math

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    k = np.array(k)
    pmf = np.exp(-lam) * (lam ** k) / math.factorial(k)
    cdf = np.array([np.exp(-lam) * (lam ** i) / math.factorial(i) for i in range(k + 1)]).sum()

    return pmf, cdf