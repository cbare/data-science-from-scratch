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

    m = number of experiments
    n = sample size, number of trials in each experiment
    p = probability of successful trial
    """
    for n,marker in zip([100,500,1000,5000],['-','--',':','-.']):
        ps = [0.4 + i/300  for i in range(60)]
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
    plt.xlabel('probability of successful trial (p)')
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


def confidence_interval(n, m, p=0.5, confidence=0.95):
    """
    How often does "fair" (0.5) lie within the confidence interval?

    m = number of experiments
    n = number of trials in an experiment
    p = true probability of success
    confidence = size of confidence interval
    """
    fair = 0
    for _ in range(m):
        p_hat = binomial(n, p) / n
        sigma_hat = math.sqrt(p_hat * (1 - p_hat) / (n-1))
        lo, hi = normal_two_sided_bounds(confidence, mu=p_hat, sigma=sigma_hat)
        fair += 1 if lo <= 0.5 <= hi else 0
    return fair / m


def estimated_parameters(N, n):
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma

def a_b_test_statistic(N_A, n_A, N_B, n_B):
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A**2 + sigma_B**2)


def B(alpha, beta):
    """a normalizing constant so that the total probability is 1"""
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)


def beta_pdf(x, alpha, beta):
    if x < 0 or x > 1: # no weight outside of [0, 1]
        return 0
    return x**(alpha-1) * (1-x)**(beta-1) / B(alpha, beta)


def plot_beta_distributions():
    params = [
        (1, 1),
        (10, 10),
        (4, 16),
        (16, 4)]
    markers = ['-','--',':','-.']
    xs = [i/100 for i in range(100)]
    for (alpha, beta), marker in zip(params, markers):
        pd = [beta_pdf(x, alpha, beta) for x in xs]
        label = f'beta({alpha}, {beta})'
        plt.plot(xs, pd, marker, label=label)

    plt.legend(loc=2)
    plt.title('Beta distributions')
    plt.show()


def updating_belief(n, p=0.75, alpha=1, beta=1):
    """
    Plot updating beliefs starting with a prior alpha and beta
    and updating with 'n' observations.
    """
    xs = [i/100 for i in range(100)]
    pd = [beta_pdf(x, alpha, beta) for x in xs]
    label = f'beta({alpha}, {beta})'
    color = (0x33/255, 0x66/255, 0x99/255, 55/255)
    plt.plot(xs, pd, label=label, color=color)
    for i in range(1, n):
        outcome = bernoulli_trial(p)
        alpha += 1 if outcome else 0
        beta += 0 if outcome else 1

        if i % 10 == 0:
            pd = [beta_pdf(x, alpha, beta) for x in xs]
            label = f'beta({alpha}, {beta})'
            color = (0x33/255, 0x66/255, 0x99/255, int(55+i/n*200)/255)
            plt.plot(xs, pd, label=label, color=color)

    plt.legend(loc=2)
    plt.title('Updating belief')
    plt.show()
