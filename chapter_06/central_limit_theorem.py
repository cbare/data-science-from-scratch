"""
Central limit theorem

Code from Chapter 6 of Data Science from Scratch
"""
import math
import random
from collections import Counter
import matplotlib.pyplot as plt


def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

def make_hist(p, n, num_points):
    data = [binomial(n, p) for _ in range(num_points)]

    # use a bar chart to show the actual binomial samples
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
            [v / num_points for v in histogram.values()],
            0.8,
            color='0.75')

    mu=p*n
    sigma = math.sqrt(n * p * (1 - p))

    # use a line chart to show the normal approximation
    # We're using CDF on narrow intervals, maybe because the binomial distribution
    # is discrete?
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
          for i in xs]
    plt.plot(xs,ys,'.')

    # We can also plot the normal pdf
    ys = [normal_pdf(i, mu, sigma) for i in xs]
    plt.plot(xs,ys)

    plt.title("Binomial Distribution vs. Normal Approximation")
    plt.show()

if __name__ == '__main__':
    make_hist(0.75, 100, 10000)
