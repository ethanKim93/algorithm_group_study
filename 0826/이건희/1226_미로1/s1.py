import sys

sys.stdin = open("input.txt")


def DFS(idx, idy):
    global ans, temps

    if [idx, idy] == [goal_r, goal_c]:
        ans = 1
        return

    for i in range(4):
        nr = idx + dirs[i][0]
        nc = idy + dirs[i][1]
        if 0 <= nr < 16 and 0 <= nc < 16:
            if maps[nr][nc] == 0 and temps[nr][nc] == 0:
                temps[nr][nc] = 1
                DFS(nr, nc)
                temps[nr][nc] = 0


for _ in range(1, 11):
    tc = int(input())
    maps = [list(map(int, input())) for _ in range(16)]
    temps = [[0] * 16 for _ in range(16)]
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    ans = 0
    for i in range(16):
        for x in range(16):
            if maps[i][x] == 2:
                start_r, start_c = i, x
                maps[i][x] = 0
            elif maps[i][x] == 3:
                goal_r, goal_c = i, x
                maps[i][x] = 0

    DFS(start_r, start_c - 1)

    print("#{} {}".format(tc, ans))
