import sys

sys.stdin = open("input.txt")


def DFS(start):
    global ans
    if start == goal:
        ans = 1
        return

    else:
        for i in range(4):
            nr = start[0] + dirs[i][0]
            nc = start[1] + dirs[i][1]
            if 0 <= nr < n and 0 <= nc < n:
                if maps[nr][nc] != "1" and not temps[nr][nc]:
                    temps[nr][nc] = True
                    DFS([nr, nc])
                    temps[nr][nc] = False


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    maps = [list(input()) for _ in range(n)]
    temps = [[0] * n for _ in range(n)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ans = 0
    for i in range(n):
        for x in range(n):
            if maps[i][x] == '2':
                start = [i, x]
            if maps[i][x] == '3':
                goal = [i, x]

    DFS(start)
    print("#{} {}".format(tc, ans))
