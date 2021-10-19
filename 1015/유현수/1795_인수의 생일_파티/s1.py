import sys
sys.stdin = open('input.txt')


def dijkstra(s, adj):
    route = [0] * (N+1)
    route[s] = 1
    cost = [INF] * (N+1)
    cost[s] = 0

    for i in range(N+1):
        if adj[s][i]:
            cost[i] = adj[s][i]

    for _ in range(N):
        w = 0
        minV = INF
        for i in range(N+1):
            if minV > cost[i] and not route[i]:
                minV = cost[i]
                w = i
        route[w] = 1

        for v in range(N+1):
            if 0 < adj[w][v] < INF:
                cost[v] = min(cost[v], cost[w] + adj[w][v])
    return cost


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    adj1 = [[0] * (N+1) for _ in range(N+1)]
    adj2 = [[0] * (N+1) for _ in range(N+1)]
    for i in range(M):
        x, y, c = map(int, input().split())
        adj1[x][y] = c
        adj2[y][x] = c
    INF = 10000000

    ans = []
    c1 = dijkstra(X, adj1)
    c2 = dijkstra(X, adj2)
    for i in range(1, N+1):
        ans.append(c1[i] + c2[i])

    print('#{} {}'.format(tc, max(ans)))
