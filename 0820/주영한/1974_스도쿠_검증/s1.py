import sys
sys.stdin = open("input.txt")


def row_col_check(matrix_input):
    for i in range(9):
        row_checker = [0] * 9
        col_checker = [0] * 9
        for j in range(9):
            row_temp = matrix_input[i][j]
            col_temp = matrix_input[j][i]
            if row_checker[row_temp] or col_checker[col_temp]:
                return 0
            row_checker[row_temp] += 1
            col_checker[col_temp] += 1
    return 1


def section_check(matrix_input):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            checker = [0] * 9
            for sub_r in range(3):
                for sub_c in range(3):
                    temp = matrix[i + sub_r][j + sub_c]
                    if checker[temp] :
                        return 0
                    checker[temp] += 1
    return 1

T = int(input())
for tc in range(1, T + 1):
    matrix = [list(map(lambda x : int(x) - 1, input().split())) for _ in range(9)]
    print("#{} {}".format(tc, row_col_check(matrix) and section_check(matrix)))
