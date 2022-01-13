import random
from math import sqrt


def mean(data):
    return sum(data) / len(data)


def variance(data):
    mu = mean(data)
    return sum([(x - mu) ** 2 for x in data]) / len(data)


def stddev(data):
    return sqrt(variance(data))


weight = [80., 85, 200, 85, 69, 65, 68, 66, 85, 72, 85, 82, 65, 105, 75, 80,
          70, 74, 72, 70, 80, 60, 80, 75, 80, 78, 63, 88.65, 90, 89, 91, 1.00E+22,
          75, 75, 90, 80, 75, -1.00E+22, -1.00E+22, -1.00E+22, 86.54, 67, 70, 92, 70, 76, 81, 93,
          70, 85, 75, 76, 79, 89, 80, 73.6, 80, 80, 120, 80, 70, 110, 65, 80,
          250, 80, 85, 81, 80, 85, 80, 90, 85, 85, 82, 83, 80, 160, 75, 75,
          80, 85, 90, 80, 89, 70, 90, 100, 70, 80, 77, 95, 120, 250, 60]


def calculate_weight(data, z):
    data.sort()
    # remove outliers
    lower_quartile = int((len(data) + 1) // 4)
    upper_quartile = int(((len(data) + 1) * 3) // 4)

    # extract data between lower and upper quartile
    data = data[lower_quartile:upper_quartile]

    # fit Gaussian using MLE
    mu = mean(data)
    standard_deviation = stddev(data)

    # compute x that corresponds to standard score z
    x = z * standard_deviation + mu

    return x

print(calculate_weight(weight, -2.))
