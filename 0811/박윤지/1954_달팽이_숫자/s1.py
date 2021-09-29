import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    cnt = 1
    i, j = 0, -1
    k = 0

    snail = [[0] * N for _ in range(N)]

    while cnt <= N*N:
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and snail[ni][nj] == 0:
            snail[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj
        else:
            k = (k + 1) % 4
    print('#{}'.format(tc))
    for row in snail:
        for num in row:
            print(num, end=' ')
        print()