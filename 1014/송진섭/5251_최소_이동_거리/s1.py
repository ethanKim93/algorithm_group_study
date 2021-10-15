"""
3
2 3
0 1 1
0 2 6
1 2 1
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
"""


def dijkstra(s, e):                                 # s: 출발지, e: 도착지
    U = [0] * (e+1)
    U[s] = 1                                        # U: 선택 정점 집합

    for v in range(e+1):
        D[v] = adj[s][v]                            # D에 출발지와 인접한 거리저장

    for _ in range(e):                              # 도착지-1만큼 반복
        minV = INF                                  # 아직 혼자 구현 x
        for i in range(e+1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                w = i
        U[w] = 1

        for v in range(e+1):                         # w에 인접하면 거쳐가는 것과 바로가는 거리 비교
            if 0 < adj[w][v] < INF:
                D[v] = min(D[v], D[w]+adj[w][v])

T = int(input())
for tc in range(1, T+1):

    INF = 1000000
    V, E = map(int, input().split())
    adj = [[INF]*(V+1) for _ in range(V+1)]         # 인접행렬 생성
    for i in range(V+1):
        adj[i][i] = 0
    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u][v] = w                               # 인접행렬 해당 거리 저장

    D = [0]*(V+1)
    dijkstra(0, V)
    print('#{} {}'.format(tc, D[-1]))