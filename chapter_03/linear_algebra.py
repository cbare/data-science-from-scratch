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
    sum multiple vectors, but uglier and gets slower as len(vectors) increases
    maybe (wild guess) due to locality?
    """
    return [sum(v_is) for v_is in zip(*vectors)]

# worrying about performance here is pointless
def _compare_vector_sum_implementations(vector_len, num_of_vectors):
    import timeit

    lots_of_vectors = [[random.random() for i in range(1000)] for _ in range(1000)]
    return {
        'vector sum by reduce': timeit.timeit(lambda : vector_sum(lots_of_vectors), number=10),
        'vector sum by zip': timeit.timeit(lambda : vector_sum_by_zip(lots_of_vectors), number=10)
    }

# thousand_vectors = [[random.random() for i in range(1000)] for _ in range(1000)]
# timeit.timeit(lambda : vector_sum(thousand_vectors), number=10)
# # 1.4608692380134016
# timeit.timeit(lambda : vector_sum_by_zip(thousand_vectors), number=10)
# # 1.1761664520017803

# ten_thousand_vectors = [[random.random() for i in range(1000)] for _ in range(10000)]
# timeit.timeit(lambda : vector_sum(ten_thousand_vectors), number=10)
# # 14.543270260968711
# timeit.timeit(lambda : vector_sum_by_zip(ten_thousand_vectors), number=10)
# # 32.18798152200179


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

