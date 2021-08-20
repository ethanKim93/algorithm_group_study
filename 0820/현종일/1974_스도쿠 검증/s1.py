import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    field = [list(map(int, input().split())) for _ in range(9)]

    result = 1
    box = [0, 3, 6]
    for i in range(9):
        col_arr = [0] * 10
        row_arr = [0] * 10
        for j in range(9):
            box_arr = [0] * 10
            if col_arr[field[j][i]] or row_arr[field[i][j]]:
                result = 0
            col_arr[field[j][i]] = 1
            row_arr[field[i][j]] = 1

            if i in box and j in box:
                for k in range(3):
                    for l in range(3):
                        if box_arr[field[i+k][j+l]]:
                            result = 0
                        box_arr[field[i+k][j+l]] = 1

    print('#{} {}'.format(tc, result))