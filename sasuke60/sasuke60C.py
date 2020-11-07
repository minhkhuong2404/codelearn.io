def maxArray(arr):
    maxx = max(arr)
    pos = arr.index(maxx)
    arr.remove(maxx)
    for i in arr:
        if i*2 > maxx:
            return -1
    return pos