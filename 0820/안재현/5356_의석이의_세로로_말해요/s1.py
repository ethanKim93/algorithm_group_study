import sys

sys.stdin = open("sample_input.txt")


T = int(input())

for tc in range(1, 1 + T):
    word2 = []
    word3 = []
    for i in range(5):
        word1 = str(input())
        for j in range(len(word1)):
            word2.append(word1[j])
        word3.append(word2)
        word2 = []

    max_len = 0
    empty = []

    for word in word3:
        empty.append(len(word))
        if len(word) > max_len:
            max_len = len(word)

    res = ''
    for q in range(max_len):
        for w in range(5):
            if empty[w] > q:
                res += word3[w][q]

    print('#{} {}'.format(tc, res))