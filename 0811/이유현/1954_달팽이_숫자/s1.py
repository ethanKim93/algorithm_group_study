import sys
sys.stdin = open('input.txt')

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)]

    cnt = 1
    i, j = 0, -1
    k = 0

    while cnt <= N*N:
        ni, nj = i+di[k], j+dj[k]
        if (ni in range(N)) and (nj in range(N)) and arr[ni][nj] == 0:
            arr[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj
        else:
            i = ni - di[k]
            j = nj - dj[k]
            k = (k+1) % 4

    print('#{}'.format(tc))
    for row in arr:
        print(*row)

