def consecutiveEvens(arr):
    maxx = -1
    now = 0
    for num in arr:
        if num % 2 == 0:
            now += 1
        else:
            if maxx < now:
                maxx = now
            now = 0
    return len(arr) if maxx == -1 else maxx

