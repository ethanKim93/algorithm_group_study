import sys
sys.stdin = open('sample_input.txt')


def ok(x, y):
    return 0 <= x < N and 0 <= y < N and maze[x][y] != 1


def bfs(idx, idy):
    queue = []
    visited = [[0] * (N) for _ in range(N)]
    queue.append((idx, idy))
    visited[idx][idy] = 1
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            new_x = x + dr[i]
            new_y = y + dc[i]
            if ok(new_x, new_y) and visited[new_x][new_y] == 0:
                queue.append((new_x, new_y))
                visited[new_x][new_y] = visited[x][y] + 1
                if maze[new_x][new_y] == 3:
                    return visited[new_x][new_y] - 2
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                idx, idy = r, c

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    print('#{} {}'.format(tc, bfs(idx, idy)))
