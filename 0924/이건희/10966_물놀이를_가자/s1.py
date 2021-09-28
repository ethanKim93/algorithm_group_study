import sys
from collections import deque
sys.stdin = open("input.txt")

def BFS(idx, idy):
    q = deque([[idx,idy]])
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dirs[i][0]
            nc = c + dirs[i][1]
            if 0 <= nr < n and 0 <= nc < m:
                if maps[nr][nc] != "W":
                    if maps[nr][nc] == "L" or maps[r][c] + 1 < maps[nr][nc]:
                        maps[nr][nc] = maps[r][c] + 1
                        q.append([nr,nc])

for tc in range(1, int(input())+1):
    n, m = map(int,input().split())
    dirs = [(0,1),(-1,0),(0,-1),(1,0)]
    maps = [list(input()) for _ in range(n)]
    for i in range(n):
        for x in range(m):
            if maps[i][x] == "W":
                maps[i][x] = 0
                BFS(i, x)
                maps[i][x] = "W"

    ans = 0

    for i in range(n):
        for x in range(m):
            if maps[i][x] != "W":
                ans += maps[i][x]
    print("#{} {}".format(tc, ans))

# Fail: Time Over