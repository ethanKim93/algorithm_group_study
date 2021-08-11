import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    arr_sum = []

    # 행, 열 합
    for i in range(100):
        row_sum = 0
        col_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        arr_sum.append(row_sum)
        arr_sum.append(col_sum)

    # 대각선 합
    dia_sum1 = 0
    dia_sum2 = 0
    for i in range(100):
        dia_sum1 += arr[i][i]
        dia_sum2 += arr[i][100-1-i]
    arr_sum.append(dia_sum1)
    arr_sum.append(dia_sum2)

    # 최댓값 구하기
    max_num = arr_sum[0]
    for num in arr_sum:
        if num > max_num:
            max_num = num

    print('#{} {}'.format(tc, max_num))