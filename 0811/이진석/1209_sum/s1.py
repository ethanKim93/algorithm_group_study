import sys

sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = int(input())
    arr = []
    max_sum = 0
    for i in range(100):
        arr.append(list(map(int, input().split())))

    for i in range(100):
        temp_sum = [0, 0, 0, 0]
        for j in range(100):
            temp_sum[0] += arr[i][j]  # 행 합
            temp_sum[1] += arr[j][i]  # 열 합
            temp_sum[2] += arr[j][j]  # 좌상 > 우하 합
            temp_sum[3] += arr[100 - j - 1][100 - j - 1]  # 좌하 > 우상 합
        for temp in temp_sum:
            if max_sum < temp:
                max_sum = temp
    print('#{} {}'.format(tc, max_sum))
