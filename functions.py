from math import sqrt
def prod_non_zero_diag(x):
    """Compute product of nonzero elements from matrix diagonal.

    input:
    x -- 2-d numpy array
    output:
    product -- integer number


    Not vectorized implementation.
    """
    sum = 1
    for i in range(min(len(x),len(x[0]))):
        if(x[i][i] != 0):
            sum *= x[i][i]
    return sum


def are_multisets_equal(x, y):
    """Return True if both vectors create equal multisets.

    input:
    x, y -- 1-d numpy arrays
    output:
    True if multisets are equal, False otherwise -- boolean

    Not vectorized implementation.
    """
    x = sorted(x)
    y = sorted(y)
    return x == y
    


def max_after_zero(x):
    """Find max element after zero in array.

    input:
    x -- 1-d numpy array
    output:
    maximum element after zero -- integer number

    Not vectorized implementation.
    """
    ans = -100000000
    for i in range(1, len(x)):
        if(x[i-1] == 0):
            if(x[i] > ans and x[i] != 0):
                ans = x[i] 
    return ans

def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """

    new_vec = [[0] * len(img[0]) for _ in range(len(img))]
    for i in range(len(img)):
        for j in range(len(img[0])):
            sum = 0
            for n in range(3):
                sum += img[i][j][n] * coefs[n]
            new_vec[i][j] = sum
    return new_vec


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Not vectorized implementation.
    """
    value = []
    quantity = []
    num = x[0]
    cnt = 1
    for i in range(1, len(x)):
        if(num != x[i]):
            value.append(num)
            quantity.append(cnt)
            num = x[i]
            cnt = 1
        else:
            cnt += 1
    value.append(num)
    quantity.append(cnt)
    return (value, quantity)
            
          

def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Not vectorized implementation.
    """
    sum = 0
    for i in range(len(x)):
        sum += (x[i] - y[i]) ** 2
    sum = sqrt(sum)
    return sum
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
