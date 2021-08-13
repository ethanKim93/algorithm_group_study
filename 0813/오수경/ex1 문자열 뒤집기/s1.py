# slicing 사용
def reverse_slicing():
    word = input()
    return word[::-1]


# temp 사용
def reverse_temp():
    words_lst = []
    words = input()
    for w in words:
        words_lst.append(w)

    temp = []
    for idx in range(int(len(words_lst)/2)):
        temp = words_lst[idx]
        words_lst[idx] = words_lst[len(words_lst)-1-idx]
        words_lst[len(words)-1-idx] = temp

    reverse_word = ''.join(words_lst)
    return reverse_word



