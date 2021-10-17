import sys
sys.stdin = open('input.txt')


def dijkstra(s, V, adj, D):                                 # 시작정점 s, 마지막 정점 V
    U = [0] * (V+1)
    U[s] = 1

    for v in range(V+1):
        D[v] = adj[s][v]

    for _ in range(V):                              # V = 정점개수-1과 같으므로..남은 정점개수와 같음
        minV = INF
        w = 0
        for i in range(V+1):
            if U[i]==0 and minV>D[i]:
                minV = D[i]
                w = i
        U[w] = 1                                    # 선택된 집합에 포함

        for v in range(V+1):                        # 정점 v가
            if 0<adj[w][v]<INF:                     # w에 인접이면 , 시작정점에서 w를 거쳐 v로 가능 비용과
                D[v] = min(D[v], D[w]+adj[w][v])    # 시작정점에서 v로 가는 기존 비용을 비교 후 선택


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())     # N 집 개수 M 경로의 수  X 인수 집
    INF = 10000000
    adj1 = [[INF] * (N+1) for _ in range(N+1)]
    adj2 = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        adj1[i][i] = 0
        adj2[i][i] = 0
    for _ in range(M):
        x, y, c = map(int, input().split())
        adj1[x][y] = c
        adj2[y][x] = c

    D1 = [0] * (N+1)
    D2 = [0] * (N+1)
    dijkstra(X, N, adj1, D1)
    dijkstra(X, N, adj2, D2)
    # print(D1)
    # print(D2)
    max_v = 0
    for i in range(1, N+1):
        v = D1[i] + D2[i]
        if v > max_v:
            max_v = v
    print('#{} {}'.format(tc, max_v))
