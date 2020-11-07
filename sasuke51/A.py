def countOdd(l,r):
    if (l % 2 == 0 and r % 2 == 0):
        return (r - l) / 2
    else:
        return (r - l) // 2 + 1