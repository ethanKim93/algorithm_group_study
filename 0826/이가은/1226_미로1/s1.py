import sys
sys.stdin = open('input.txt')

def road_find(sy,sx):
    d = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    que = [[sy, sx]]
    visited = [[0]*16 for _ in range(16)]
    visited[sy][sx] = 1

    while que:
        my, mx = que.pop(0)

        for i in range(4):
            ny = my + d[i][0]
            nx = mx + d[i][1]

            if -1 < ny < 16 and -1 < nx < 16 and (maze[ny][nx] == 0 or maze[ny][nx] == 3) and not (visited[ny][nx]):
                que.append([ny, nx])
                if maze[ny][nx] == 3:
                    return 1
                else:
                    maze[ny][nx] = 1
                    visited[ny][nx] = 1
    return 0

for _ in range(10):
    tc = input()

    maze = [list(int(char) for char in input()) for _ in range(16)]

    for y in range(16):
        for x in range(16):
            if maze[y][x] == 2:
                sy = y
                sx = x
    print('#{} {}'.format(tc, road_find(sy,sx)))