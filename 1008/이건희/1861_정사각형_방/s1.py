import sys
sys.stdin = open("input.txt")
sys.setrecursionlimit(100000)

def DFS(idx,idy,cnt_idx,cnt):
    global ans, ans_idx
    if cnt > ans:
        ans = cnt
        ans_idx = cnt_idx

    elif ans == cnt:
        if ans_idx > cnt_idx:
            ans_idx = cnt_idx

    for i in range(4):
        nr = idx + dirs[i][0]
        nc = idy + dirs[i][1]
        if 0 <= nr < n and 0 <= nc < n:
            if maps[nr][nc] == maps[idx][idy] + 1:
                DFS(nr,nc,cnt_idx,cnt+1)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    maps = [list(map(int,input().split())) for _ in range(n)]
    ans_idx = 987654321
    ans = 0

    for i in range(n):
        for x in range(n):
            DFS(i,x,maps[i][x],1)

    print("#{} {} {}".format(tc, ans_idx, ans))

# Pass