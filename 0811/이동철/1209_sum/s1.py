import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    #가로 행의 합
    max_row = 0
    for i in range(100):
        sum_row = 0
        for j in range(100):
            sum_row += arr[i][j]
        if sum_row > max_row:
            max_row = sum_row

    # 세로줄의 합
    max_col = 0
    for i in range(100):
        sum_col = 0
        for j in range(100):
            sum_col += arr[j][i]
        if sum_col > max_col:
            max_col = sum_col
    
    # 대각선의 합
    max_r_c = 0
    sum1 = 0
    sum2 = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                sum1 += arr[i][j]
            elif i + j == 99:
                sum2 += arr[i][j]
    if max(sum1, sum2) > max_r_c:
        max_r_c = max(sum1, sum2)

    print('#{} {}'.format(T, max(max_row, max_col, max_r_c)))
