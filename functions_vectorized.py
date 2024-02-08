import numpy as np
from math import sqrt

def prod_non_zero_diag(x):
    """Compute product of nonzero elements from matrix diagonal.

    input:
    x -- 2-d numpy array
    output:
    product -- integer number


    Vectorized implementation.
    """
    diag = np.diag(x)
    return diag[diag != 0].prod()

def are_multisets_equal(x, y):
    """Return True if both vectors create equal multisets.

    input:
    x, y -- 1-d numpy arrays
    output:
    True if multisets are equal, False otherwise -- boolean

    Vectorized implementation.
    """
    x = np.sort(x)
    y = np.sort(y)
    return np.array_equal(x, y)

 
def max_after_zero(arr):
    """Find max element after zero in array.

    input:
    x -- 1-d numpy array
    output:
    maximum element after zero -- integer number

    Vectorized implementation.
    """
    zero_indices = np.where(arr == 0)[0]
    
    if len(zero_indices) == 0:
        return None
    
    zero_indices_shifted = zero_indices + 1
    
    valid_zero_indices = zero_indices_shifted[zero_indices_shifted < len(arr)]
    
    if len(valid_zero_indices) == 0:
        return None
   
    max_after_zero = np.max(arr[valid_zero_indices])
    
    return max_after_zero


def convert_image(image, weights):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Vectorized implementation.
    """

    weighted_channels = image * weights
    
    grayscale_image = np.sum(weighted_channels, axis=2)
    
    return grayscale_image


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Vectorized implementation.
    """
    vec = np.append(-1, np.where(x[1:] != x[:-1]))
    vec = np.append(vec, len(x)-1)
    return (x[vec], np.diff(vec))

def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    V{e}ctorized implementation.
    """
    vec = x - y
    vec = vec * vec
    vec = np.sum(vec)
    return sqrt(vec)
    









