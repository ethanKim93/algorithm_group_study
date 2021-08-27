import sys
sys.stdin = open('input.txt')


def ok(x, y):
    return 0 <= x < 16 and 0 <= y < 16 and maze[x][y] != 1


def bfs(start_x, start_y):
    queue = []
    visited = [[0] * 16 for _ in range(16)]
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            new_x = x + dr[i]
            new_y = y + dc[i]
            if ok(new_x, new_y) and visited[new_x][new_y] == 0:
                queue.append((new_x, new_y))
                visited[new_x][new_y] = visited[x][y] + 1
                if maze[new_x][new_y] == 3:
                    return 1
    return 0


for tc in range(1, 10 + 1):
    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    for r in range(16):
        for c in range(16):
            if maze[r][c] == 2:
                start_x, start_y = r, c

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    print('#{} {}'.format(tc, bfs(start_x, start_y)))
