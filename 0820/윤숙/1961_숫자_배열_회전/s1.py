import sys

sys.stdin = open('input.txt')
T = int(input())


def round90(arr, N):
    change = [[0] * N for _ in range(N)]
    for i in range(N - 1, -1, -1):
        for j in range(N):
            change[i][j] = arr[N - 1 - j][i]

    return change


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result1 = round90(arr, N)
    result2 = round90(result1, N)
    result3 = round90(result2, N)

    print('#{}'.format(tc))
    for i in range(N):
        print(''.join(map(str,result1[i])), ''.join(map(str,result2[i])), ''.join(map(str,result3[i])))
