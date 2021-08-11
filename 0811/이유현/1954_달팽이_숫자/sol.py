import sys
sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)]
    arr[0][0] = 1

    r, c = 0, 0
    n = 1

    while n < N*N:
        for i in range(4):
            r += dr[i]
            c += dc[i]

            while (0 <= r < N and 0 <= c < N) and not arr[r][c]:
                n += 1
                arr[r][c] = n

                r += dr[i]
                c += dc[i]
            r -= dr[i]
            c -= dc[i]
    print('#{}'.format(tc))
    for row in arr:
        print(*row)

