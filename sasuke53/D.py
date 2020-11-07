def intersect_circle(a,b):
    if a[2] <= 0 or b[2] <= 0:
        return False
    dis = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    radSum = (a[2] + b[2]) ** 2
    radSub = abs((a[2] - b[2])) ** 2
    if dis > radSum or dis < radSub:
        return False
    else:
        return True
