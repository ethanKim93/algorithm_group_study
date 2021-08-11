import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    A = [[0] * N for _ in range(N)]
    cnt = 1
    k = 0
    i, j = 0, -1
    while cnt <= N*N:
        ni, nj = i+di[k], j+dj[k]  # type: (int, int)
        if (0 <= ni < N) and (0 <= nj < N) and (A[ni][nj] == 0):
            A[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj
        else:
            k = (k+1) % 4
    print('#{}'.format(tc))
    for matrix in A:
        print(*matrix)
