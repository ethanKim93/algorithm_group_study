import sys
sys.stdin = open("input.txt")
from collections import deque


def bfs(start):
    q = deque()
    q.append(start)
    temps[start[0]][start[1]] = 0
    while q:
        idx, idy = q.popleft()
        for i in range(4):
            nr = idx + dirs[i][0]
            nc = idy + dirs[i][1]
            if 0 <= nr < n and 0 <= nc < n:
                if temps[nr][nc] > temps[idx][idy] + maps[nr][nc]:
                    temps[nr][nc] = temps[idx][idy] + maps[nr][nc]
                    q.append([nr, nc])
    return temps[n - 1][n - 1]


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    maps = [list(map(int, input())) for _ in range(n)]
    inf = 9923999329
    temps = [[inf] * n for _ in range(n)]
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    print("#{} {}".format(tc, bfs([0, 0])))
