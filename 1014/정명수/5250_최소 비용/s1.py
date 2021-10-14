import sys
sys.stdin = open('input.txt')

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs():
    q = [(0,0)]
    visit[0][0] = 0
    while q:
        r,c = q.pop(0)
        for i in range(4):
            dr = r+dx[i]
            dc = c+dy[i]
            if 0<=dr<N and 0<=dc<N:
                diff = arr[dr][dc]-arr[r][c]
                if diff>0:
                    if visit[dr][dc]>visit[r][c]+diff+1:
                        visit[dr][dc] = visit[r][c]+diff+1
                        q.append((dr,dc))
                else:
                    if visit[dr][dc]>visit[r][c]+1:
                        visit[dr][dc] = visit[r][c]+1
                        q.append((dr,dc))


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visit = [[10000]*N for _ in range(N)]
    dfs()
    print('#{} {}'.format(tc,visit[N-1][N-1]))

