import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    c_num, c_length = map(str, input().split())
    case = input().split()

    for i in range(len(case)):
        if case[i] == "ZRO":
            case[i] = 0
        if case[i] == "ONE":
            case[i] = 1
        if case[i] == "TWO":
            case[i] = 2
        if case[i] == "THR":
            case[i] = 3
        if case[i] == "FOR":
            case[i] = 4
        if case[i] == "FIV":
            case[i] = 5
        if case[i] == "SIX":
            case[i] = 6
        if case[i] == "SVN":
            case[i] = 7
        if case[i] == "EGT":
            case[i] = 8
        if case[i] == "NIN":
            case[i] = 9

    for i in range(0, len(case) -1):
        min_num = i
        for j in range(i+1, len(case)):
            if case[min_num] > case[j]:
                min_num = j
        case[i], case[min_num] = case[min_num], case[i]

    for i in range(len(case)):
        if case[i] == 0:
            case[i] = "ZRO"
        if case[i] == 1:
            case[i] = "ONE"
        if case[i] == 2:
            case[i] = "TWO"
        if case[i] == 3:
            case[i] = "THR"
        if case[i] == 4:
            case[i] = "FOR"
        if case[i] == 5:
            case[i] = "FIV"
        if case[i] == 6:
            case[i] = "SIX"
        if case[i] == 7:
            case[i] = "SVN"
        if case[i] == 8:
            case[i] = "EGT"
        if case[i] == 9:
            case[i] = "NIN"

    print('#{}'.format(tc))
    print(*case)
