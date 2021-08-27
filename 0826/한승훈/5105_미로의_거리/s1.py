import sys
sys.stdin = open('sample_input.txt')


def move(u, v):
    queue = []
    visited.append((u, v))
    queue.append((u, v))

    while queue:
        now_x, now_y = queue.pop(0)
        for idx in range(4):
            ni, nj = now_x + dx[idx], now_y + dy[idx]
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] in [0, 3]:
                if (ni, nj) not in visited:
                    queue.append((ni, nj))
                    visited.append((ni, nj))
                    distance[ni][nj] = distance[now_x][now_y] + 1
                    if (ni, nj) == end:
                        return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [[] for _ in range(N)]
    for i in range(N):
        maze[i].extend(map(int, input()))
    ans = 0
    dx = [0, 0, -1, 1]  # 우 좌 상 하
    dy = [1, -1, 0, 0]
    for x in range(N):
        for y in range(N):
            if maze[x][y] == 2:
                start = (x, y)  # 시작지점의 인덱스값
            elif maze[x][y] == 3:
                end = (x, y)
    visited = []
    distance = [[0] * N for _ in range(N)]
    move(start[0], start[1])

    if distance[end[0]][end[1]]:
        ans = distance[end[0]][end[1]] - 1
    else:
        ans = 0
    print('#{} {}'.format(tc, ans))