import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    p = np.array(p)
    x = np.array(x)

    if p.sum() != 1:
        raise ValueError(f"[Error] The Sum of Probability vector p needs to add up to 1. Currently it adds up to {p.sum()} for {p}")
    
    return (x * p).sum()