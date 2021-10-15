import sys
from collections import deque

sys.stdin = open("input.txt")
cnt = 0

def bfs(start):
    q = deque()
    q.append(start)
    temps = [[inf] * n for _ in range(n)]
    temps[start[0]][start[1]] = maps[start[0]][start[1]]
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dirs[i][0]
            nc = c + dirs[i][1]
            if 0 <= nr < n and 0 <= nc < n:
                if temps[nr][nc] > temps[r][c] + maps[nr][nc]:
                    temps[nr][nc] = temps[r][c] + maps[nr][nc]
                    q.append([nr, nc])
    return temps[n - 1][n - 1]

while True:
    cnt += 1
    n = int(input())
    if n == 0:
        break
    maps = [list(map(int, input().split())) for _ in range(n)]
    inf = 98585372842
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    print("Problem {}: {}".format(cnt, bfs([0, 0])))

# Pass