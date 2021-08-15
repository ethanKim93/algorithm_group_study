# 되긴 하는데 검색 시간 초과

import sys

sys.stdin = open('GNS_test_input.txt', 'rt', encoding='UTF8')


def Ntrans(w):
    if w == "ZRO":
        return 0
    elif w == "ONE":
        return 1
    elif w == "TWO":
        return 2
    elif w == "THR":
        return 3
    elif w == "FOR":
        return 4
    elif w == "FIV":
        return 5
    elif w == "SIX":
        return 6
    elif w == "SVN":
        return 7
    elif w == "EGT":
        return 8
    elif w == "NIN":
        return 9


def Wtrans(w):
    if w == 0:
        return "ZRO"
    elif w == 1:
        return "ONE"
    elif w == 2:
        return "TWO"
    elif w == 3:
        return "THR"
    elif w == 4:
        return "FOR"
    elif w == 5:
        return "FIV"
    elif w == 6:
        return "SIX"
    elif w == 7:
        return "SVN"
    elif w == 8:
        return "EGT"
    elif w == 9:
        return "NIN"


T = int(input())

empty_list = []
result = ''
for tc in range(0, T):
    R1, R2 = input().split()
    A = [list(input().split())]
    for i in range(len(A[0])):
        empty_list.append(Ntrans(A[0][i]))

    empty_list = sorted(empty_list)

    # print('#{} {}'.format(tc+1, empty_list))
    for i in range(len(empty_list)):
        result += Wtrans(empty_list[i])
        result += ' '
    print('#{} {}'.format(tc + 1, result))
    result = ''
