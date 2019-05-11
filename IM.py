
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

"""
val_x_data = np.random.uniform(0, 1, (60000, 32, 32))
val_y_data = np.random.randint(0, 5, (60000))

print(val_x_data.shape, val_y_data.shape)
"""
num_friends = [100,49,41,40,25,60]


num_points = len(num_friends)
l_v = max(num_friends)
s_v = min(num_friends)


def mean(x):
    return sum(x) / len(x)

mean(num_friends)
def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2
median(num_friends)

def qu(x,p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]
qu(num_friends, 0.10)

def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems()
            if count == max_count]
mode(num_friends)


def data_range(x):
    return max(x) - min(x)
data_range(num_friends)

def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]
def vari(x):
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)
vari(num_friends)

def standard_deviation(x):
    return math.aqrt(vari(x))
standard_deviation(num_friends)

def inter_range(x):
    return qu(x,0.75) - qu(x, 0.25)
inter_range(num_friends)

def con(x, y):
    n = len(x)
    return dot(de_mean(x),de_mean(y)) / (n - 1)
con(num_friends,daily_minutes)

def predict(alpha, beta, x_i):
    return beta * x_i + alpha
def error(alpha, beta, x_i, y_i):
    return y_i - predict(alpha, beta, x_i)

def sum_of_squared(alpha, beta, x,y):
    return sum(error(alpha, beta, x_i, y_i) ** 2
                    for x_i, y_i in zip(x,y))

def least_squares_fit(x,y):
    beta = corretion(x,y) * standard_deviation(y) / standard_deviation(x)
    alpha = mean(y) - beta * mean(x)
    return alpha, beta
alpha, beta = least_squares_fit(num_friends_good, daily_minutes_good)

print(alpha)
print(beta)