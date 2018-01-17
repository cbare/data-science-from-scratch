"""
Hypothesis Testing

Code from Chapter 7 of Data Science from Scratch
"""
from normal import normal_cdf, inverse_normal_cdf
from central_limit_theorem import binomial
import math, random


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


def plot_detect_biased_coin():
    """
    Empirically test how often a test at a p-value of 0.05 would
    call a coin fair at varying levels of bias for each of 4
    sample sizes.
    """
    for n,marker in zip([100,500,1000,5000],['-','--',':','-.']):
        ps = [0.4 + i*0.2/24 for i in range(25)]
        looks_fair_percent = []
        mu_0, sigma_0 = normal_approximation_to_binomial(n, 0.5)
        for p in ps:
            data = [binomial(n,p) for _ in range(1000)]
            looks_fair_percent.append(
                sum(between(normal_two_sided_bounds(0.95, mu_0, sigma_0), d) for d in data)/1000)

        plt.plot(ps,looks_fair_percent,marker,label='n={}'.format(n))

    plt.legend(loc=2)
    plt.title('How much bias can we detect?')
    plt.ylabel('fraction of experiments that look fair')
    plt.xlabel('p')
    plt.show()
