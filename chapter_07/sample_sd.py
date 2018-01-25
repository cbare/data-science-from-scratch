"""
Sample variance and standard deviation.

When we compute sample standard deviation, we
use a denominator of (n-1). Is that really a better
estimate of population sd? Let's find out.
"""
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from stats import *
from normal import normal_pdf

# a population of 1 million
pop = np.fromiter((random.random() for _ in range(1000000)), float)

print('population mean = ', pop.mean())
print('population std = ', pop.std())

def standard_deviation_alt(xs):
    n = len(xs)
    mu = sum(xs)/n
    return math.sqrt(sum((x-mu)**2 for x in xs) / n)

n = 10

# plot density of sd's computed using a denominator of n-1.
sample_stds_1 = np.fromiter(
    (standard_deviation(np.random.choice(pop, n, replace=False))
    for _ in range(1000)), float)
sns.kdeplot(sample_stds_1, shade=True, color='skyblue',
    label='denom = (n-1)')

# now plot density of sd's computed using a denominator of n.
sample_stds_2 = np.fromiter(
    (standard_deviation_alt(np.random.choice(pop, n, replace=False))
    for _ in range(1000)), float)
sns.kdeplot(sample_stds_2, shade=True, color='springgreen',
    label='denom = n')

plt.axvline(x=pop.std())
plt.title('Why we use a denominator of (n-1) to compute sample standard deviation')
plt.show()
