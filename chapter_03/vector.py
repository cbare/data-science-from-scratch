"""
Vector arithmetic

Code from Chapter 2 of Data Science from Scratch
"""
import math
from functools import reduce


# Implement vector arithmetic. It's "from scratch".
# Joel represents vectors as Python lists. Would tuples be more natural?

def vector_add(v, w):
    """
    add vectors element-wise
    """
    return [v_i + w_i for v_i,w_i in zip(v,w)]

def vector_subtract(v, w):
    """
    subtract vectors element-wise
    """
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    """
    sum multiple vectors
    """
    return reduce(vector_add, vectors)

def vector_sum_by_zip(vectors):
    """
    sum multiple vectors, but uglier and slower as the number of vectors increase.
    """
    return [sum(v_is) for v_is in zip(*vectors)]

def scalar_multiply(c, v):
    """
    multiple a vector v by a scalar c
    """
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """compute the vector whose ith element is the mean of the ith elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
    """
    dot product of v and w
    """
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return magnitude(vector_subtract(v, w))
    # equivalent to
    # return math.sqrt(squared_distance(v, w))

