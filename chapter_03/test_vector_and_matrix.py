"""
Test vector and matrix operations
"""
from matrix import *
from vector import dot


def test_matrix_multiple():
    A = [[1, 2], [3, 4]]
    B = [[2, 0], [1, 2]]
    assert matrix_multiply(A, B) == [[4, 4], [10, 8]]

    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    assert matrix_multiply(A, B) == [[58, 64], [139, 154]]

    A = [[3, 4, 2]]
    B = [[13, 9, 7, 15], [8, 7, 4, 6], [6, 4, 0, 3]]
    assert matrix_multiply(A, B) == [[83, 63, 37, 75]]


# worrying about performance here is silly, but...
def _compare_vector_sum_implementations(vector_len, num_of_vectors, number=100):
    import timeit

    lots_of_vectors = [[random.random() for i in range(vector_len)] for _ in range(num_of_vectors)]
    return (timeit.timeit(lambda : vector_sum(lots_of_vectors), number=number) / number,
            timeit.timeit(lambda : vector_sum_by_zip(lots_of_vectors), number=number) / number)

def _test_perf_vector_sum():
    # Outputs:

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
    import tabulate

    perf = [(vector_len, num_of_vectors)+_compare_vector_sum_implementations(vector_len, num_of_vectors, number=100)
            for vector_len in (10, 100, 1000)
            for num_of_vectors in (10, 100, 1000, 5000, 10000)]
    print(tabulate(perf, headers='vector_len, num_of_vectors, reduce, zip'.split(', '), floatfmt=".5f"))
