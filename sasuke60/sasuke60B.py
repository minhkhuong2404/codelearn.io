def reverseString(str, k):
    new_str = ""
    last_char = 0
    first_char = 0
    time = 0
    while last_char <= len(str):
        last_char += k
        time += 1
        if time % 2 == 1:
            new_str += ''.join(reversed(str[first_char:last_char]))
        else:
            new_str += str[first_char:last_char]
        first_char += k
        print(new_str)

    return new_str