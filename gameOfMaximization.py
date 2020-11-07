def gameOfMaximization(arr):
    item = []
    for i in range(3):
        item.append(sum(arr[i::3]))

    return int(min(item) * 3)