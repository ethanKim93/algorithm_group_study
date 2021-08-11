import sys
sys.stdin = open('input.txt')

for _ in range(10):
    test_case = int(input())

    mat = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0
    # 행의 합 검사
    for arr in mat:
        if sum(arr) > max_sum:
            max_sum = sum(arr)

    # 열의 합 검사
    for j in range(100):
        j_sum = 0
        for i in range(100):
            j_sum += mat[i][j]
        if j_sum > max_sum:
            max_sum = j_sum

    #\ 대각선 합 검사
    temp_sum_1 = 0
    for i in range(100):
        temp_sum_1 += mat[i][i]
    if temp_sum_1 > max_sum:
        max_sum = temp_sum_1

    # /대각선 합 검사
    temp_sum_2 = 0
    for i in range(100):
        temp_sum_2 += mat[i][99 - i]
    if temp_sum_2 > max_sum:
        max_sum = temp_sum_2

    print('#{} {}'.format(test_case+1, max_sum))
