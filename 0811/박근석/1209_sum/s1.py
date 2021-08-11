import sys
sys.stdin = open('input.txt')


for k in range(1, 11):
    T = input()

    list_a = []

    A = [0]*100
    for i in range(100):
        A[i] = list(map(int, input().split()))

    for i in range(100):
        total = 0
        for j in range(100):
            total += A[i][j]
        list_a.append(total)

    for j in range(100):
        total = 0
        for i in range(100):
            total += A[i][j]
        list_a.append(total)

    total = 0
    for i in range(100):
        total += A[i][i]
    list_a.append(total)

    total = 0
    for i in range(100):
        total += A[i][100-i-1]
    list_a.append(total)

    max_num = list_a[0]
    for i in list_a:
        if i > max_num:
            max_num = i

    print('#{} {}'.format(k, max_num))















