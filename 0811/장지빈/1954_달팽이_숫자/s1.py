import sys
sys.stdin = open('input.txt')


dx = [0, 1, 0, -1]  # 상우하좌
dy = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]
    snail[0][0] = 1
    x = y = 0
    go = 0
    num = 2

    while num <= N**2:
        if 0 <= x + dx[go % 4] < N and 0 <= y +dy[go % 4] < N and not snail[x + dx[go % 4]][y + dy[go % 4]]:
            x += dx[go % 4]
            y += dy[go % 4]
            snail[x][y] = num
            num += 1
        else:
            go += 1

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(snail[i][j], end=' ')
        print()
