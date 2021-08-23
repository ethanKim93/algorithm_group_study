import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(0, T):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]

    result = 0

    for i in range(0, n // 2):
        for j in range(i + 1):
            if j == 0:
                result += farm[i][n // 2]

            else:
                result += farm[i][n // 2 + j]
                result += farm[i][n // 2 - j]

    for k in range(n):
        result += farm[n // 2][k]

    for l in range(n // 2 + 1, n):
        for q in range(n - l):
            if q == 0:
                result += farm[l][n // 2]
            else:
                result += farm[l][n // 2 + q]
                result += farm[l][n // 2 - q]

    print('#{} {}'.format(tc + 1, result))