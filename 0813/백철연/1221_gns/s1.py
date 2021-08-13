import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

alpha = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, 1 + T):

    n = list(map(str, input().split()))

    number_list = list(map(str, input().split()))

    res = []

    for q in range(10):
        for w in number_list:
            if alpha[q] == w:
                res.append(w)

    print('#{}'.format(tc))
    print(*res)
