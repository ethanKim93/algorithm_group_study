import sys
from collections import deque
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    n, m, r, c, l = map(int,input().split())
    maps = [list(map(int,input().split())) for _ in range(n)]
    temps = [["NO"]*m for _ in range(n)]
    dirs = [0,(-1,0),(0,1),(1,0),(0,-1)]
    from_turnel = [[0],[1,2,3,4],[1,3],[2,4],[4,3],[1,4],[2,1],[2,3]] # 처음: 0, 상: 1, 우:2, 하: 3, 좌: 4
    go_turnel = [[0],[1,2,3,4],[1,3],[2,4],[1,2],[2,3],[3,4],[1,4]] # 처음: 0, 상: 1, 우:2, 하: 3, 좌: 4
    q = deque([])
    q.append([r,c])
    temps[r][c] = 0
    while q:
        r, c, = q.popleft()
        for i in range(1,5):
            if i in go_turnel[maps[r][c]]:
                nr = r + dirs[i][0]
                nc = c + dirs[i][1]
                if 0 <= nr < n and 0 <= nc < m:
                    if maps[nr][nc] != 0 and temps[nr][nc] == "NO":
                        if i in from_turnel[maps[nr][nc]]:
                            q.append([nr,nc])
                            temps[nr][nc] = temps[r][c] + 1

    ans = 0
    for i in range(n):
        for x in range(m):
            if type(temps[i][x]) == int:
                if temps[i][x] <= l-1:
                    ans += 1

    print("#{} {}".format(tc,ans))
# Pass