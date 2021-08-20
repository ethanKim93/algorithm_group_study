import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    field = [list(map(int, input().split())) for _ in range(9)]

    result = 1
    box = [0, 3, 6]
    for i in range(9):
        colsum = 0
        rowsum = 0
        flag = False
        for j in range(9):
            boxsum = 0
            colsum += field[j][i]
            rowsum += field[i][j]

            if i in box and j in box:
                for k in range(3):
                    for l in range(3):
                        boxsum += field[i+k][j+l]
                if boxsum != 45:
                    flag = True

        if colsum != 45 or rowsum != 45 or flag:
            result = 0
            break

    print('#{} {}'.format(tc, result))