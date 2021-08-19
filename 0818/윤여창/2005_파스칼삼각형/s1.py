import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    p = [[0]*10 for _ in range(10)]

    for i in range(10):
        for j in range(i + 1):
            if j == 0 or i == j:
                p[i][j] = 1
            else:
                p[i][j] = p[i - 1][j - 1] + p[i - 1][j]

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(i+1):
            print(p[i][j], end = ' ')
        print()