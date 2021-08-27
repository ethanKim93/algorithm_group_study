import sys
sys.stdin = open('input.txt')


def move(x, y):
    global ans
    queue = []
    queue.append((x, y))
    visited.append((x, y))
    while queue:
        now_x, now_y = queue.pop(0)
        for idx in range(4):
            ni, nj = now_x + dx[idx], now_y + dy[idx]
            if 0 <= ni < 16 and 0 <= nj < 16 and maze[ni][nj] in [0, 3]:
                if (ni, nj) not in visited:
                    visited.append((ni, nj))
                    queue.append((ni, nj))
                if (ni, nj) == end:
                    ans = 1
                    return


for _ in range(10):
    tc = int(input())
    maze = [[] * 16 for _ in range(16)]
    for i in range(16):
        maze[i].extend(map(int, input()))

    for x in range(16):
        for y in range(16):
            if maze[x][y] == 2:
                start = (x, y)
            elif maze[x][y] == 3:
                end = (x, y)
    visited = []
    ans = 0
    dx = [0, 0, -1, 1]  # 우 좌 상 하
    dy = [1, -1, 0, 0]
    move(start[0], start[1])
    print('#{} {}'.format(tc, ans))
