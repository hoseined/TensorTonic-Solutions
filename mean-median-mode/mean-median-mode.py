import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.array(x)
    counts = Counter(x)
    mode = counts.most_common(1)[0][0]
    return x.mean(), np.median(x), mode