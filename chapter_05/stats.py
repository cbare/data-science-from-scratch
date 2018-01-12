"""
Stats

Code from Chapter 5 of Data Science from Scratch
"""
import math
from collections import Counter
from vector import dot

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

def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems()
            if count == max_count]

def de_mean(xs):
    mu = mean(xs)
    return ((x-mu) for x in xs)

def variance(xs):
    mu = mean(xs)
    n = len(xs)
    return sum((x-mu)**2 for x in xs) / (n-1)

def standard_deviation(xs):
    return math.sqrt(variance(xs))

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n-1)

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero
