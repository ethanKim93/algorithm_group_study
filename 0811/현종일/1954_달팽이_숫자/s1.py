import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [0, 1, 0, -1]  # 우 하 좌 상
dy = [1, 0, -1, 0]

for tc in range(1, T+1):
    print('#{}'.format(tc))

    N = int(input())
    arr = [[0] * N for _ in range(N)]
    x, y = 0, 0
    dire = 0

    for n in range(1, N**2 + 1):
        arr[x][y] = n
        x += dx[dire]
        y += dy[dire]

        if x < 0 or y < 0 or x >= N or y >= N or arr[x][y] != 0:
            x -= dx[dire]
            y -= dy[dire]

            dire = (dire + 1) % 4

            x += dx[dire]
            y += dy[dire]

    for j in arr:
        print('{}'.format(' '.join(map(str,j))))


