import sys
sys.stdin = open('input.txt')

dr = [-1, 0, 0]
dc = [0, 1, -1]

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    r = 99
    x2 = 0
    for i in range(100):
        if arr[99][i] == 2:
            x2 = i
    k = 0
    while r >= 0:
        r += dr[k]
        x2 += dc[k]

        while (0 <= r and 0 <= x2 < 100) and arr[r][x2]:
            if k == 0:
                if 0 <= r and (0 <= x2+1 < 100) and arr[r][x2+1]:
                    k = 1
                    r += dr[k]
                    x2 += dc[k]

                elif 0 <= r and (0 <= x2-1 < 100) and arr[r][x2-1]:
                    k = 2
                    r += dr[k]
                    x2 += dc[k]
                else:
                    r += dr[k]
                    x2 += dc[k]

            if k == 1 or k == 2:
                if 0 <= r-1 and (0 <= x2 < 100) and arr[r-1][x2]:
                    k = 0
                    r += dr[k]
                    x2 += dc[k]

                else:
                    r += dr[k]
                    x2 += dc[k]
        r -= dr[k]
        x2 -= dc[k]

        if r == 0:
            break
    print('#{} {}'.format(tc, x2))