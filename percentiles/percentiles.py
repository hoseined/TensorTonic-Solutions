import numpy as np
import math

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    input_array = np.array(x)
    percentile_array = np.array(q)
    input_array = np.sort(input_array)
    array_lenth = len(input_array)
    percentile_array = (percentile_array / 100) * (array_lenth - 1)

    def get_percentile_value(arr, percentile):
        floor = math.floor(percentile)
        ceil = math.ceil(percentile)

        if floor == ceil:
            return arr[floor]
        else:
            weight = percentile - floor
            return (1 - weight) * arr[floor] + weight * arr[ceil]

    return np.array([get_percentile_value(input_array, item) for item in percentile_array])