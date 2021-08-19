import sys

sys.stdin = open('input.txt')
T = int(input())


def pascal(n):
    N = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                N[i][j] = 1
            else:
                N[i][j] = N[i - 1][j] + N[i - 1][j - 1]
    return N


for tc in range(1, T + 1):
    n = int(input())
    print('#{}'.format(tc))
    for pascal_lst in pascal(n):
        for num in pascal_lst:
            if num:
                print(num, end=' ')
        print()

