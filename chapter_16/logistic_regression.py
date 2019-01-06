import random

from stats import mean, median, de_mean, standard_deviation, correlation
from gradient_descent import minimize_stochastic
from vector import dot, vector_add
from normal import normal_cdf
from matrix import make_matrix, get_column, shape, matrix_multiply


def scale(data):
    num_rows, num_cols = shape(data)
    means = [mean(get_column(data, j)) for j in range(num_cols)]
    stdevs = [standard_deviation(get_column(data, j)) for j in range(num_cols)]
    return means, stdevs

def rescale(data):
    """
    rescales the input data so that each column has mean 0 and standard deviation 1
    leaves alone columns with no deviation
    """
    means, stdevs = scale(data)
    
    def rescaled(i, j):
        if stdevs[j] > 0:
            return (data[i][j] - means[j]) / stdevs[j]
        else:
            return data[i][j]

    num_rows, num_cols = shape(data)
    return make_matrix(num_rows, num_cols, rescaled)


def error(x_i, y_i, beta):
    return y_i - predict(x_i, beta)


def squared_error(x_i, y_i, beta):
    return error(x_i, y_i, beta) ** 2


def squared_error_gradient(x_i, y_i, beta):
    """the gradient (with respect to beta) corresponding to the ith squared error term"""
    return [-2 * x_ij * error(x_i, y_i, beta)
            for x_ij in x_i]


def predict(x_i, beta):
    """assumes that the first element of each x_i is 1"""
    return dot(x_i, beta)


def estimate_beta(x, y):
    beta_initial = [random.random() for x_i in x[0]]
    return minimize_stochastic(squared_error,
                               squared_error_gradient,
                               x, y,
                               beta_initial,
                               0.001)

def split_data(data, prob):
    """
    split data into fractions [prob, 1 - prob]
    """
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results

def train_test_split(x, y, test_pct):
    """
    Make train/test split.
    """
    data = zip(x, y)
    train, test = split_data(data, 1 - test_pct)
    x_train, y_train = zip(*train)
    x_test, y_test = zip(*test)
    return x_train, x_test, y_train, y_test

