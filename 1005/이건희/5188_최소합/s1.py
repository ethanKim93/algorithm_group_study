import sys
sys.stdin = open("input.txt")

def DFS(idx, idy, total):
    global ans
    if total >= ans:
        return

    if idx == goal_x and idy == goal_y:
        total = total + maps[idx][idy]
        if ans > total:
            ans = total
            return

    for i in range(2):
        nr = idx + dirs[i][0]
        nc = idy + dirs[i][1]
        if 0 <= nr < n and 0 <= nc < n:
            if not temps[nr][nc]:
                temps[nr][nc] = 1
                DFS(nr,nc,total+maps[idx][idy])
                temps[nr][nc] = 0



t = int(input())
for tc in range(1,t+1):
    n = int(input())
    maps = [list(map(int,input().split())) for _ in range(n)]
    temps = [[0]*n for _ in range(n)]
    dirs = [(0,1),(1,0)]
    start_x, start_y = 0, 0
    goal_x, goal_y = n-1, n-1
    ans = 1690
    DFS(start_x, start_y, 0)
    print("#{} {}".format(tc,ans))