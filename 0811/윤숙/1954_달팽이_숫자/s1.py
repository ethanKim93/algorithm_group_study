import sys

sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    x,y,direction=0,0,0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for cnt in range(1, n * n + 1):
        arr[x][y] = cnt
        x += dx[direction]
        y += dy[direction]

        if x < 0 or y < 0 or x >= n or y >= n or arr[x][y]!=0:
            x -= dx[direction]
            y -= dy[direction]

            direction = (direction + 1) % 4
            x += dx[direction]
            y += dy[direction]

    for i in arr:
        print(*i, ' ')