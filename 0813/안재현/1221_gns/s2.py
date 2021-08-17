

import sys

sys.stdin = open('GNS_test_input.txt', 'rt', encoding='UTF8')


T = int(input())


def Sort(x):
    for i in range(len(x) - 1, 0, -1):
        for j in range(i):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x


for test_case in range(1, T + 1):

    N, K = map(str, input().split())
    K = int(K)
    result = list(map(str, input().split()))

    for i in range(K):
        if result[i] == 'ZRO':
            result[i] = 0
        elif result[i] == 'ONE':
            result[i] = 1
        elif result[i] == 'TWO':
            result[i] = 2
        elif result[i] == 'THR':
            result[i] = 3
        elif result[i] == 'FOR':
            result[i] = 4
        elif result[i] == 'FIV':
            result[i] = 5
        elif result[i] == 'SIX':
            result[i] = 6
        elif result[i] == 'SVN':
            result[i] = 7
        elif result[i] == 'EGT':
            result[i] = 8
        else:
            result[i] = 9

    Sort(result)

    for j in range(K):
        if result[j] == 0:
            result[j] = 'ZRO'
        elif result[j] == 1:
            result[j] = 'ONE'
        elif result[j] == 2:
            result[j] = 'TWO'
        elif result[j] == 3:
            result[j] = 'THR'
        elif result[j] == 4:
            result[j] = 'FOR'
        elif result[j] == 5:
            result[j] = 'FIV'
        elif result[j] == 6:
            result[j] = 'SIX'
        elif result[j] == 7:
            result[j] = 'SVN'
        elif result[j] == 8:
            result[j] = 'EGT'
        else:
            result[j] = 'NIN'

    print(N)
    for k in range(K):
        print(result[k], end=' ')