import sys
sys.stdin = open('sample_input.txt')


def bfs():
    visit = [[0] * N for _ in range(N)]
    route = []
    route.append(start)
    visit[start[0]][start[1]] = 1

    dr = [-1, 0, 0, 1]
    dc = [0, 1, -1, 0]
    while route:
        now = route.pop(0)

        for d in range(4):
            nr, nc = now[0] + dr[d], now[1] + dc[d]
            if nr in range(N) and nc in range(N):
                if visit[nr][nc] == 0 and (maze[nr][nc] == 0 or maze[nr][nc] == 3):
                    route.append([nr, nc])
                    visit[nr][nc] = visit[now[0]][now[1]] + 1

                    if [nr, nc] == end:
                        return visit
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = [i, j]
            if maze[i][j] == 3:
                end = [i, j]

    if bfs():
        cnt = bfs()[end[0]][end[1]] - 2
    else:
        cnt = 0

    print('#{} {}'.format(tc, cnt))
