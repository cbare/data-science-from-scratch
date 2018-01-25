"""
Compare population mean with sample mean
"""
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from stats import *
from normal import normal_pdf

# a population of 1 million
pop = [random.random() for _ in range(1000000)]

population_mean = sum(pop)/len(pop)
print('population mean = ', population_mean)

n = 100
sample_means = np.fromiter((sum(random.sample(pop, k=n))/n for _ in range(1000)), float)

# make a pretty picture
sns.kdeplot(sample_means, shade=True, color='skyblue',
    label='probability density of sampling distribution')

# estimate the standard deviation of the sampling distribution
sd = standard_deviation(pop)/math.sqrt(n)
xs = [x/500 + 0.4 for x in range(100)]
plt.plot(xs,
    [normal_pdf(x, mu=population_mean, sigma=sd) for x in xs],
    '--',
    color='#30336699',
    label=f'normal mu={population_mean:0.3} sigma={sd:0.3}')

plt.axvline(x=population_mean)
plt.title('Probability density of sample means vs. population mean')
plt.legend(loc=2)
plt.show()
