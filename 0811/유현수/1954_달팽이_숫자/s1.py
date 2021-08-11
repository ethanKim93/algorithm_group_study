import sys
sys.stdin=open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    snail = [[0] * N for i in range(N)]

    r, c = 0, -1
    idx = 0
    num = 1
    while num < N**2+1:
        r += dr[idx % 4]
        c += dc[idx % 4]
        if r < 0 or r >= N or c < 0 or c >= N:
            r -= dr[idx % 4]
            c -= dc[idx % 4]
            idx += 1
        elif snail[r][c]:
            r -= dr[idx % 4]
            c -= dc[idx % 4]
            idx += 1
        else:
            snail[r][c] = num
            num += 1

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(snail[i][j], end=' ')
        print()