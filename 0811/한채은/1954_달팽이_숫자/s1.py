import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    mode = 0

    x = 0
    y = 0

    snail[x][y] = 1

    for i in range(2, N**2+1):
        x += dx[mode]
        y += dy[mode]

        snail[x][y] = i

        if 0 <= x + dx[mode] < N and 0 <= y + dy[mode] < N and not snail[x + dx[mode]][y + dy[mode]]:
            continue

        if mode != 3:
            mode += 1

        else:
            mode = 0

    print('#{}'.format(tc))
    for j in snail:
        print(*j)