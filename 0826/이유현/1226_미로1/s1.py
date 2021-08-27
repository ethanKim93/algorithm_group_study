import sys
sys.stdin = open('input.txt')

# dfs
def dfs():
    route = []
    route.append(start)

    dr = [-1, 0, 0, 1]
    dc = [0, 1, -1, 0]
    while route:
        now = route.pop()
        visit[now[0]][now[1]] = 1

        for d in range(4):
            nr, nc = now[0] + dr[d], now[1] + dc[d]
            if nr in range(16) and nc in range(16):
                if visit[nr][nc] == 0 and (maze[nr][nc] == 0 or maze[nr][nc] == 3):
                    route.append([nr, nc])

    if visit[end[0]][end[1]] == 1:
        return 1
    else:
        return 0


for tc in range(1, 11):
    tn = input()
    maze = [list(map(int, input())) for _ in range(16)]
    visit = [[0] * 16 for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start = [i, j]
            if maze[i][j] == 3:
                end = [i, j]
    print('#{} {}'.format(tc, dfs()))