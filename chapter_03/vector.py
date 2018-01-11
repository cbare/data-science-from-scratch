"""
Linear Algebra

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


# worrying about performance here is silly, but...
def _compare_vector_sum_implementations(vector_len, num_of_vectors, number=100):
    import timeit

    lots_of_vectors = [[random.random() for i in range(vector_len)] for _ in range(num_of_vectors)]
    return (timeit.timeit(lambda : vector_sum(lots_of_vectors), number=number) / number,
            timeit.timeit(lambda : vector_sum_by_zip(lots_of_vectors), number=number) / number)

def _be_silly():
    import tabulate

    perf = [(vector_len, num_of_vectors)+_compare_vector_sum_implementations(vector_len, num_of_vectors, number=100)
            for vector_len in (10, 100, 1000)
            for num_of_vectors in (10, 100, 1000, 5000, 10000)]
    print(tabulate(perf, headers='vector_len, num_of_vectors, reduce, zip'.split(', '), floatfmt=".5f"))

#   vector_len    num_of_vectors    reduce      zip
# ------------  ----------------  --------  -------
#           10                10   0.00001  0.00000
#           10               100   0.00015  0.00002
#           10              1000   0.00183  0.00029
#           10              5000   0.00913  0.00266
#           10             10000   0.01617  0.00869
#          100                10   0.00009  0.00005
#          100               100   0.00093  0.00021
#          100              1000   0.00984  0.00400
#          100              5000   0.06485  0.09937
#          100             10000   0.14297  0.23023
#         1000                10   0.00132  0.00056
#         1000               100   0.01388  0.00429
#         1000              1000   0.13434  0.11415
#         1000              5000   0.66533  1.35771
#         1000             10000   1.42573  3.34425

# What do we learn from this?

# The zip implementation starts out faster, but looses out as the size and
# number of vectors increases. This might have something to do with loss of
# locality due to iterating over vectors in the inner loop.


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

