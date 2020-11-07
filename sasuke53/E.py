def numberSequence(arr,k):
    new_arr = []
    set_new_arr = set(new_arr)
    now = 1
    add_zero = False
    if len(arr) == 1:
        return int(str(arr[0])*k)

    if arr.count(0) == 0:
        arr.append(0)
        add_zero = True
    arr.sort()
    for a in range(0, len(arr)):
        for b in range(0, len(arr)):
            for c in range(0, len(arr)):
                for d in range(0, len(arr)):
                    for e in range(0, len(arr)):
                        for f in range(0, len(arr)):
                            num = str(arr[a]) + str(arr[b]) + str(arr[c]) + str(arr[d]) + str(arr[e]) + str(arr[f])
                            start = [x for x in num if x != "0"]
                            if len(start) > 0:
                                str_start = "".join(str(s) for s in start)
                                if add_zero == True:
                                    set_new_arr.add(int(str_start))
                                else:
                                    set_new_arr.add(int(num))
                                    set_new_arr.add(0)
                            if len(set_new_arr) > k:
                                # print(set_new_arr)
                                new = list(set_new_arr)
                                new.sort()
                                print(new)
                                return new[k-1]