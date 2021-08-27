import sys
sys.stdin = open('input.txt')


def dfs():
    visit = [[0] * 100 for _ in range(100)]
    route = [start]

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while route:
        now = route.pop()
        visit[now[0]][now[1]] = 1

        for d in range(4):
            nr, nc = now[0] + dr[d], now[1] + dc[d]
            if nr in range(101) and nc in range(101):
                if not visit[nr][nc] and (maze[nr][nc] == 0 or maze[nr][nc] == 3):
                    route.append([nr, nc])

                    if [nr, nc] == end:
                        return 1
    return 0


for tc in range(1, 11):
    tn = input()
    maze = [list(map(int, input())) for _ in range(100)]

    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                start = [i, j]
            if maze[i][j] == 3:
                end = [i, j]

    print('#{} {}'.format(tc, dfs()))


