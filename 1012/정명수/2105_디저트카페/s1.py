import sys
sys.stdin = open('input.txt')
dx = [1,1,-1,-1]
dy = [1,-1,-1,1]
def desert(i,j,visited,now_direction=0):
    global max_route,start_j,start_i
    if i==start_i and j==start_j:
        max_route = max(max_route,len(visited))
    for x in range(4):
        di = i+dx[x]
        dj = j+dy[x]
        if 0<=di<N and 0<=dj<N and arr[di][dj] not in visited:
            if x == now_direction or x == now_direction+1:
                desert(di,dj,visited+[arr[di][dj]],x)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = []
    max_route = 0
    for start_i in range(N):
        for start_j in range(N):
            desert(start_i,start_j,[])
    if not max_route:
        max_route = -1
    print("#{} {}".format(tc,max_route))