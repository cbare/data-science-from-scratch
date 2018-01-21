"""
Normal distributions

Code from Chapter 6 of Data Science from Scratch
"""
import math
import random
import matplotlib.pyplot as plt


def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))


def normal_cdf(x, mu=0,sigma=1):
    """cummulative density function"""
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """find approximate inverse using binary search"""

    low_z, low_p = -10.0, 0
    hi_z, hi_p = 10.0, 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            # midpoint is still too low, search above it
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # midpoint is still too high, search below it
            hi_z, hi_p = mid_z, mid_p
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mu + sigma * mid_z


if __name__ == '__main__':
    xs = [x / 10.0 for x in range(-50, 50)]

    plt.plot(xs,[normal_pdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
    plt.plot(xs,[normal_pdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
    plt.plot(xs,[normal_pdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
    plt.plot(xs,[normal_pdf(x,mu=-1) for x in xs],'-.',label='mu=-1,sigma=1')
    plt.legend()
    plt.title("Various Normal pdfs")
    plt.show()

    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs,[normal_cdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
    plt.plot(xs,[normal_cdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
    plt.plot(xs,[normal_cdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
    plt.plot(xs,[normal_cdf(x,mu=-1) for x in xs],'-.',label='mu=-1,sigma=1')
    plt.legend(loc=4) # bottom right
    plt.title("Various Normal cdfs")
    plt.show()

    inverse_normal_cdf(0.25)
    # -0.6744861602783203
    inverse_normal_cdf(0.5)
    # 0.0
    inverse_normal_cdf(0.66)
    # 0.41245460510253906
    inverse_normal_cdf(0.9)
    # 1.2815570831298828
    inverse_normal_cdf(0.95)
    # 1.6448497772216797
    inverse_normal_cdf(0.99)
    # 2.326345443725586

    # does it work?
    n = 10000
    sum(random.gauss(0,1) <= -0.6744861602783203 for _ in range(n))/n
    0.2507
    sum(random.gauss(0,1) <= 0.0 for _ in range(n))/n
    0.4969
    sum(random.gauss(0,1) <= 0.41245460510253906 for _ in range(n))/n
    0.6609
    sum(random.gauss(0,1) <= 1.2815570831298828 for _ in range(n))/n
    0.8993
    sum(random.gauss(0,1) <= 1.6448497772216797 for _ in range(n))/n
    0.9497
