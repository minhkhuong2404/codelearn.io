def arithmeticSequence(arr):
    b = []
    for i in range(0, len(arr)):
        b.append(arr[i])

    b.sort()

    d = []
    for i in range(0, len(arr)):
        d.append(arr[i])

    d.sort(reverse = True)

    add = True
    diff = b[1] - b[0]
    if b.count(b[0]) == len(b):
        return True
    for i in range(1, len(b)):
        if b[i] - b[i-1] != diff:
            add = False

    ct = 0
    cd = 0
    for i in range(0, len(arr)):
        if arr[i] != b[i]:
            ct += 1
        if arr[i] != d[i]:
            cd += 1

    if (ct == 2 and add) or (cd == 2 and add):
        return True
    else:
        return False