import sys
sys.stdin = open("input.txt")
#5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리
def dijkstra(s):
    visited[s] = True

    for i in range(N+1):        # s에서 갈 수 있는 곳을 베이스로 distance에 기록
        if adjMatrix[s][i]:
            distance[i] = adjMatrix[s][i]

    for _ in range(N+1):
        minIdx = 0
        minV = inf
        for i in range(N+1):
            if minV > adjMatrix[s][i] and not visited[i]: # 가진값보다 작은값 and 방문 X
                minV = adjMatrix[s][i]
                minIdx = i
        visited[minIdx] = True

        for v in range(N+1):
            distance[v] = min(distance[v], distance[minIdx]+adjMatrix[minIdx][v])

for tc in range(1, int(input())+1):
    N, E = map(int, input().split())
    inf = 10000
    adjMatrix = [[inf]*(N+1) for _ in range(N+1)]
    visited = [False]*(N+1)
    distance = [0]*(N+1)
    for _ in range(E):
        s, e, w = map(int, input().split())
        adjMatrix[s][e] = w

    dijkstra(0)
    print('#{} {}'.format(tc, distance[N]))