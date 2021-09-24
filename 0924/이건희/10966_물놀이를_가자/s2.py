import sys
from collections import deque
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    n, m = map(int,input().split())
    dirs = [(0,1),(-1,0),(0,-1),(1,0)]
    maps = [input() for _ in range(n)]
    temps = [[10000]*m for _ in range(n)]
    q = deque([])
    for i in range(n):
        for x in range(m):
            if maps[i][x] == "W":
                q.append([i,x])
                temps[i][x] = 0
    while q:
        r, c = q.popleft()
        for y in range(4):
            nr = r + dirs[y][0]
            nc = c + dirs[y][1]
            if 0 <= nr < n and 0 <= nc < m:
                if maps[nr][nc] == "L" and temps[nr][nc] == 10000:
                    temps[nr][nc] = temps[r][c] + 1
                    q.append([nr, nc])

    ans = 0

    for i in range(n):
        for x in range(m):
            ans += temps[i][x]

    print("#{} {}".format(tc, ans))

# Pass

# Couldn't solve(testcase는 모두 통과, 제출하면 6번 이상부터 런타임에러)
# 1. 왜 maps = list input 할 때는 런타임 에러?
# 2. 왜 temps = [string] 이면 런타임 에러?
# 3. 왜 temps에서 안하고 maps에서 하면 런타임 에러?