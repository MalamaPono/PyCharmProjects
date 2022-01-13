# Write a function sample that simulates N sets of coin flips and
# returns a list of the proportion of heads in each set of N flips
# It may help to use the flip and mean functions that you wrote before

import random
from math import sqrt
from matplotlib import pyplot as plt


def mean(data):
    return float(sum(data)) / len(data)


def variance(data):
    mu = mean(data)
    return sum([(x - mu) ** 2 for x in data]) / len(data)


def stddev(data):
    return sqrt(variance(data))


def flip(N):
    return [random.random() > 0.5 for x in range(N)]


def sample(N):
    return [mean(flip(N)) for _ in range(N)]


N = 1000
outcomes = sample(N)
plt.hist(outcomes, bins=30)
plt.show()

print(mean(outcomes))
print(stddev(outcomes))