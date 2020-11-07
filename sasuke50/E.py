def findTheSquareAgain(a, b):
    new_a = [a[i:i + 2] for i in range(0, len(a), 2)]
    new_b = [b[i:i + 2] for i in range(0, len(b), 2)]

    count = 0
    same = []
    for point in new_a:
        if point in new_b:
            same += [point]
            count += 1

    for point in same:
        new_a.remove(point)
        new_b.remove(point)

    if count != 2:
        return False

    return ((pow(same[0][0] - same[1][0], 2) + pow(same[0][1] - same[1][1], 2)) == (
                pow(new_a[0][0] - new_b[0][0], 2) + pow(new_a[0][1] - new_b[0][1], 2))) and (
                       (pow(same[0][0] - new_a[0][0], 2) + pow(same[0][1] - new_a[0][1], 2)) == (
                           pow(same[1][0] - new_a[0][0], 2) + pow(same[1][1] - new_a[0][1], 2)))
