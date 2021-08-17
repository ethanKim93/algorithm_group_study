def buf(word):
    word = list(word)
    for w in range(len(word)//2):
        temp = word[-w-1]
        word[-w-1] = word[w]
        word[w] = temp
    word = ''.join(word)
    return word

print(buf('abcde'))