def gcd(a, b):
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a
def relative_number(input):
    return abs(input[1] - input[0]) == gcd(input[0], input[1])

