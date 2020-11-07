def secondMax(a):
    b = sorted(a)[-2]
    return a.index(b) + 1
