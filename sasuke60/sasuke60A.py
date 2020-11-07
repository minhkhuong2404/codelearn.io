import math


def countPoints2(n):
    if (n == 2):
        return 5

    return 1.5 * math.pow(n, 2) - 0.5 * n