import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_list = []

    for i in range(100):
        num_sum = 0
        for j in range(100):
            num_sum += arr[i][j]
        sum_list.append(num_sum)

    for j in range(100):
        num_sum = 0
        for i in range(100):
            num_sum += arr[i][j]
        sum_list.append(num_sum)

    num_sum = 0
    for i in range(100):
        num_sum += arr[i][i]
    sum_list.append(num_sum)

    num_sum = 0
    for i in range(99, -1, -1):
        num_sum += arr[i][99 - i]
    sum_list.append(num_sum)

    max_num = max(sum_list)
    print('#{} {}'.format(N, max_num))
