"""
3
5
0 0 0 0 0
0 1 2 3 0
0 2 3 4 0
0 3 4 5 0
0 0 0 0 0
5
0 1 1 1 0
1 1 0 1 0
0 1 0 1 0
1 0 0 1 1
1 1 1 1 1
"""
# 런타임에러
dr = [1, 0]              # 하 우
dc = [0, 1]


def dijkstra(s, V):
    U = [0] * (V+1)
    U[s] = 1
    for v in range(V+1):
        D[v] = adj[s][v]

    #while len(U) != V:
    for _ in range(V):
        minV = INF
        w = 0
        for i in range(V+1):
            if U[i]==0 and minV>D[i]:
                minV = D[i]
                w = i
        U[w] = 1

        for v in range(V+1):
            if 0<adj[w][v]<INF:
                D[v] = min(D[v], D[w]+adj[w][v])


T = int(input())
for tc in range(1, 1+1):
    N = int(input())
    high_info = [list(map(int, input().split())) for _ in range(N)]
    # print(tc, high_info)
    cost_info = []
    for r in range(N):
        for c in range(N):
            for k in range(2):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    cost_info.append(N*r+c)                                         # 시작점
                    cost_info.append(N*nr+nc)                                       # 이동가능 점
                    cost_info.append(abs(high_info[r][c] - high_info[nr][nc])+1)    # 기본비용: 1 높이차이에따른 비용추가
    # print(cost_info)
    INF = 10000
    V = N*N
    adj = [[INF] * (V + 1) for _ in range(V + 1)]
    for i in range(V + 1):
        adj[i][i] = 0
    for j in range(0, len(cost_info), 3):
        u, v, w = cost_info[j], cost_info[j+1], cost_info[j+2]
        adj[u][v] = w
    # print(adj)
    D = [0] * (V + 1)
    dijkstra(0, V-1)
    # print(D)
    print('#{} {}'.format(tc, D[V-1]))