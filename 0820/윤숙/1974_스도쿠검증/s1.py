import sys

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T + 1):
    quest = [list((map(int, input().split()))) for _ in range(9)]

    checked = [0] * 9
    cnt = 0
    isnot = 1

    for i in range(9):
        sum1 = 0
        checked = [0] * 10
        for j in range(9):
            sum1 += quest[i][j]
            checked[quest[i][j]] = 1
        sumc = 0
        for s in checked:
            sumc += s
        if sum1 == 45 and sumc == 9:
            cnt += 1
        elif sum1 != 45 or sumc != 9:
            isnot = 0
            break

    for i in range(9):
        sum2 = 0
        checked = [0] * 10
        for j in range(9):
            sum2 += quest[j][i]
            checked[quest[j][i]] = 1
        sumc = 0
        for s in checked:
            sumc += s
        if sum2 == 45 and sumc == 9:
            cnt += 1
        elif sum2 != 45 or sumc != 9:
            isnot = 0
            break
    for m  in range(0,9,3):
        for i in range(0,9,3):
            sumcheck = 0
            checked = [0] * 10
            for j in range(3):
                for k in range(3):
                    sumcheck += quest[i+j][m+k]
                    checked[quest[j][i]] = 1
            if sumcheck == 45 and sumc == 9:
                cnt += 1
            elif sum2 != 45  or sumc != 9:
                isnot = 0
                break

    print(isnot)
