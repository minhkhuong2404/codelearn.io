import math


def sum_of_cubes_odd_number(n):
    summ = 0
    d = math.pow(10, 9) + 7
    if n <= 0:
        return -1
    else:
        for i in range(1, n + 1):
            summ += math.pow(2 * i - 1, 3) % d
        return summ % d

