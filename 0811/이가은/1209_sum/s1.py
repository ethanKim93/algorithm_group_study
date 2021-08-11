import sys
sys.stdin = open('input.txt')

for test in range(1, 11):
    test_num = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int,input().split())))

    sum_list = []   # 각 행의 합, 각 열의 합, 각 대각선의 합을 받을 list

    # 같은 행의 합
    for row in range(100):
        sum_row = 0
        for col in range(100):
            sum_row += arr[row][col]
        sum_list.append(sum_row)

    # 같은 열의 합
    for col in range(100):
        sum_col = 0
        for row in range(100):
            sum_col += arr[row][col]
        sum_list.append(sum_col)

    # 오른쪽 아래 대각선의 합
    for i in range(100):
        sum_list.append(arr[i][i])

    # 왼쪽 아래 대각선의 합
    for j in range(100):
        sum_list.append(arr[j][99-j])

    print('#{} {}'.format(test, max(sum_list)))