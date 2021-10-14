import sys
from collections import deque

sys.stdin = open("input.txt")


def bfs(idx, idy):
    q = deque()
    q.append([idx, idy])
    temps[idx][idy] = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dirs[i][0]
            nc = c + dirs[i][1]
            if 0 <= nr < n and 0 <= nc < n:
                if maps[nr][nc] > maps[r][c]:
                    if temps[nr][nc] > temps[r][c] + maps[nr][nc] - maps[r][c] + 1:
                        temps[nr][nc] = temps[r][c] + maps[nr][nc] - maps[r][c] + 1
                        q.append([nr, nc])

                else:
                    if temps[nr][nc] > temps[r][c] + 1:
                        temps[nr][nc] = temps[r][c] + 1
                        q.append([nr, nc])

    return temps[n - 1][n - 1]


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    inf = 987654321
    temps = [[inf] * n for _ in range(n)]
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    print("#{} {}".format(tc, bfs(0, 0)))

# Pass