def countWord(str, word):
    count = 0
    counting = True
    new_str = str
    while counting:
        length = 0
        for char in word:
            # print((list_str.index(char)))
            # print(char)
            if new_str.find(char) != -1:
                length += 1
                new_str = new_str.replace(char, "", 1)
            else:
                counting = False

        if length == len(word):
            count += 1
    return count


print(countWord("loonbalxballpoon", "balloon"))
