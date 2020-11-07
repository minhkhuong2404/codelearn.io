def distributeCandy(age):
    arr = []

    for i in range(0,len(age)):
        arr.append(age[i])
    print(arr)
    candy_lr = [1]*(len(arr))
    candy_rl = [1]*(len(arr))
    candy = []

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            candy_lr[i] = candy_lr[i-1]+1

    for i in range(len(arr)-2, -1, -1):
        if arr[i] > arr[i+1]:
            candy_rl[i] = candy_rl[i+1]+1

    for i in range(0, len(arr)):
        candy.append(max(candy_lr[i], candy_rl[i]))

    return (sum(candy))