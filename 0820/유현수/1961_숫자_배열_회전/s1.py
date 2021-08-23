import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr1 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr1[i][j] = arr[N-j-1][i]

    arr2 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr2[i][j] = arr[N-i-1][N-j-1]

    arr3 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr3[i][j] = arr[j][N-i-1]

    print('#{}'.format(tc))
    for i in range(N):
        print(*arr1[i], sep='', end=' ')
        print(*arr2[i], sep='', end=' ')
        print(*arr3[i], sep='')