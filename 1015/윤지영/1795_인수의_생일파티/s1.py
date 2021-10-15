import sys
sys.stdin = open('input.txt')

def dijkstra(n,dist,arr):
    visited = [0] * (N+1)
    visited[n] = 1
    for i in range(N+1):
        dist[i] = arr[n][i]
    for _ in range(N):
        w = 0
        minV = INF
        for k in range(1,N+1):
            if visited[k] == 0 and minV > dist[k]:
                w = k
                minV = dist[k]
        visited[w] = 1
        for v in range(1,N+1):
            if 0 < arr[w][v] < INF:
                dist[v] = min(dist[v], dist[w] + arr[w][v])

T = int(input())
for tc in range(1,T+1):
    N,M,X = map(int,input().split())
    INF = 987654321
    ar = [[INF] * (N+1) for _ in range(N+1)]
    ar2 = [[INF] * (N+1) for _ in range(N+1)]
    for i in range(M):
        x,y,c= map(int,input().split())
        ar[x][y] = c
        ar2[y][x] = c
    dis = [INF] * (N+1)
    dis2 = [INF] *(N+1)
    for j in range(N+1):
        ar[j][j] = 0
        ar2[j][j] = 0
    dijkstra(X,dis,ar)      # X번 까지 가는길
    dijkstra(X,dis2,ar2)    # X번 에서 돌아오는길
    res = 0
    for k in range(1,N+1):
        if res < dis[k]+dis2[k]:
            res = dis[k] + dis2[k]
    print('#{} {}'.format(tc,res))


