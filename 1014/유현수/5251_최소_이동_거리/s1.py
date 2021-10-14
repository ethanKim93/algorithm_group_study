import sys
sys.stdin = open('sample_input.txt')


def dijkstar(s):
    route = [0] * (N+1)
    route[s] = 1

    cost = [INF] * (N+1)                                        # 시작점에서 해당 인덱스의 정점까지의 비용을 기록하는 배열
    for i in range(N+1):
        if adj[s][i]:
            cost[i] = adj[s][i]

    for _ in range(N):
        w = 0
        minV = INF
        for i in range(N+1):                                    # 모든 정점 중에서
            if minV > cost[i] and not route[i]:                 # 선택되지 않은 정점 중에 가중치(cost[i])가 가장 작은 정점 w 찾기
                minV = cost[i]
                w = i
        route[w] = 1                                            # 정점 w 선택

        for v in range(N+1):
            if 0 < adj[w][v] < INF:                             # w에 인접한 정점 v에 대해
                cost[v] = min(cost[v], cost[w] + adj[w][v])
                # cost[v] == 시작점에서 정점 v까지 필요한 비용
                # cost[w] == 시작점에서 정점 w까지 필요한 비용
                # adj[w][v] = 정점 w에서 정점 v까지 필요한 비용
                # 즉, 현재 시작점에서 v까지 필요한 비용 vs 현재 시작점 - w - v까지의 비용 중 적은 것을 cost에 기록한다는 뜻
    return cost[N]


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adj = [[0] * (N+1) for _ in range(N+1)]
    for i in range(E):
        r, c, w = map(int, input().split())
        adj[r][c] = w

    INF = 100000000
    print('#{} {}'.format(tc, dijkstar(0)))
