"""
Stats

Code from Chapter 5 of Data Science from Scratch
"""
from collections import Counter

def find_bin(x, breaks):
    """
    Return an integer indicating which 'bucket' x falls into. Buckets are
    intervals that divide the space of real numbers such that:

    [-inf, breaks_0), [breaks_0, breaks_1), [breaks_1, ..., breaks_n), [breaks_n,+inf]

    All buckets are closed on their lower bound. All buckets except the last
    are open on their upper bound.

    For examples, breaks=[10, 20] creates three buckets: numbers less than 10,
    numbers in [10, 20) and numbers >= 20.
    """
    i = len(breaks)
    while i > 0 and x < breaks[i-1]:
        i -= 1
    return i


def bin(xs, breaks):
    return [find_bin(x, breaks) for x in xs]


def hist(xs, breaks):
    return Counter(bin(xs, breaks))


def mean(x):
    return sum(x) / len(x)


def median(v):
    """finds the 'middle-most' value of v"""
    sorted_v = sorted(v)
    n = len(v)
    midpoint = n // 2

    if n % 2 == 1:
        # if odd, return the middle value
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

