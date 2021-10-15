import sys
sys.stdin = open('input.txt')

def BFS():
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = [(0,0,0)]
    INF = 23497856
    visit = [[INF]*(N+1) for _ in range(N+1)]
    visit[0][0] = 0
    while q:
        i,j,work = q.pop(0)
        for x in range(4):
            di = i+dx[x]
            dj = j+dy[x]
            if 0<=di<N and 0<=dj<N:
                next_work = work+int(arr[di][dj])
                if next_work < visit[di][dj]:
                    visit[di][dj] = next_work
                    q.append((di,dj,next_work))
    return visit[N-1][N-1]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    print('#{} {}'.format(tc,BFS()))