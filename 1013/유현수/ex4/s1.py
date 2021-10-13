import sys
sys.stdin = open('sample_input.txt')


def dijkstra(s):
    route = [0] * (V+1)
    route[s] = 1
    print(s, end=' ')
    cost = adj[s][:]                    # 시작점에서 해당 인덱스의 정점까지의 비용을 기록하는 배열
    # print(cost)

    for _ in range(V):
        w = 0
        minV = INF
        for i in range(V+1):            # 모든 정점 중에서
            if not route[i]:            # 선택되지 않은 정점 중에
                if minV > cost[i]:      # D[w] 즉, 가중치가 가장 작은 정점 w 찾기
                    w = i
                    minV = cost[w]
        route[w] = 1                    # 정점 w 선택
        print(w, end=' ')
        for v in range(V+1):
            if adj[w][v]:               # w에 인접한 정점 v에 대해
                cost[v] = min(cost[v], cost[w] + adj[w][v])
                # D[v] == 시작점에서 정점 v까지 필요한 비용
                # D[w] == 시작점에서 정점 w까지 필요한 비용
                # adj[w][v] = 정점 w에서 정점 v까지 필요한 비용
                # 즉, 현재 시작점에서 v까지 필요한 비용 vs 현재 시작점 - w - v까지의 비용 중 적은 것을 D에 기록한다는 뜻
                # print(cost)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    INF = 10000
    adj = [[INF] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        x, y, z = map(int, input().split())
        adj[x][y] = z
    for j in range(V+1):
        adj[j][j] = 0

    print('#{}'.format(tc), end=' ')
    dijkstra(0)
    print()
