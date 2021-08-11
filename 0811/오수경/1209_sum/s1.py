import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    tc_num = input()
    arr = []
    for arr_a in range(100):
        arr.append(list(map(int, input().split())))


    total_lst = []

    # 행, 열 합
    for i in range(100):
        total_a = 0
        total_b = 0
        for j in range(100):
            total_a += arr[i][j]
            total_b += arr[j][i]
        total_lst.extend([total_a, total_b])

    # \ 대각선 합
    for i in range(100):
        total = 0
        for j in range(100):
            if i == j:
                total += arr[i][j]

    # / 대각선 합 -1, 1
    i, j = -1, 100
    for k in range(100):
        i += 1
        j -= 1
        total += arr[i][j]
    total_lst.append(total)

    big = 0
    for num in total_lst:
        if num > big:
            big = num


    print('#{} {}'.format(tc, big))
