"""
Hypothesis Testing

Code from Chapter 7 of Data Science from Scratch
"""
from normal import normal_cdf, inverse_normal_cdf
from central_limit_theorem import binomial
import math, random
import matplotlib.pyplot as plt


def normal_approximation_to_binomial(n, p):
    """finds mu and sigma corresponding to a Binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma


# the normal cdf _is_ the probability the variable is below a threshold
normal_probability_below = normal_cdf


# it's above the threshold if it's not below the threshold
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)


# it's between if it's less than hi, but not less than lo
def normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)


# it's outside if it's not between
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)


def normal_upper_bound(probability, mu=0, sigma=1):
    """returns the z for which P(Z <= z) = probability"""
    return inverse_normal_cdf(probability, mu, sigma)


def normal_lower_bound(probability, mu=0, sigma=1):
    """returns the z for which P(Z >= z) = probability"""
    return inverse_normal_cdf(1 - probability, mu, sigma)


def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """returns the symmetric (about the mean) bounds
    that contain the specified probability"""
    tail_probability = (1 - probability) / 2

    # upper bound should have tail_probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    # lower bound should have tail_probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound


def plot_detect_biased_coin(m=1000):
    """
    Empirically test how often a test at a p-value of 0.05 would
    call a coin fair at varying levels of bias for each of 4
    sample sizes.
    """
    for n,marker in zip([100,500,1000,5000],['-','--',':','-.']):
        ps = (0.4 + i/300  for i in range(60))
        looks_fair_percent = []
        mu_0, sigma_0 = normal_approximation_to_binomial(n, 0.5)
        lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)
        for p in ps:
            data = [binomial(n,p) for _ in range(m)]
            looks_fair_percent.append(sum(d>lo and d<hi for d in data)/m)

        plt.plot(ps, looks_fair_percent, marker, label='n={}'.format(n))

    plt.legend(loc=2)
    plt.title('How much bias can we detect?')
    plt.ylabel('fraction of experiments that look fair')
    plt.xlabel('p')
    plt.show()


def probability_to_detect_two_sided(n, p):
    """
    Power is the probability that we will correctly reject the null hypothesis
    given a value of p and sample size n.
    """
    mu_0, sigma_0 = normal_approximation_to_binomial(n, 0.5)
    lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)
    mu_1, sigma_1 = normal_approximation_to_binomial(n, p)
    type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
    power = 1 - type_2_probability
    return power


def probability_to_detect_one_sided(n, p):
    """
    Power is the probability that we will correctly reject the null hypothesis
    given a value of p and sample size n.
    """
    mu_0, sigma_0 = normal_approximation_to_binomial(n, 0.5)
    hi = normal_upper_bound(0.95, mu_0, sigma_0)
    mu_1, sigma_1 = normal_approximation_to_binomial(n, p)
    type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
    power = 1 - type_2_probability
    return power


def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
        # if x is greater than the mean, the tail is what's greater than x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # if x is less than the mean, the tail is what's less than x
        return 2 * normal_probability_below(x, mu, sigma)


def count_extreme_values(n, p, lo, hi, m=10000):
    """
    Perform m batches of n trials where the probability of success in a trial is p.
    Return the number of batches that produce an 'extreme' value of successes as
    defined by the hi and lo cut-off values.

        In [64]: mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
        In [65]: lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)
        In [66]: lo
        Out[66]: 469.01026640487555
        In [67]: hi
        Out[67]: 530.9897335951244
        In [68]: count_extreme_values(1000, 0.5, lo, hi, m=10000)
        Out[68]: 521
        In [69]: 521/10000
        Out[69]: 0.0521

    """
    extreme_value_count = 0
    for _ in range(m):
        num_heads = sum(1 if random.random() < p else 0 for _ in range(n))
        if num_heads >= hi or num_heads <= lo:
            extreme_value_count += 1
    return extreme_value_count

