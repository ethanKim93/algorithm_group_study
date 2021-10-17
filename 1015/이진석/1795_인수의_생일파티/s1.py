import sys

sys.stdin = open('input.txt')

def dijkstra(start, adj):
    dist = [INF] * (N + 1)
    dist[start] = 0
    visited = [0] * (N+1)

    for _ in range(N):
        min_idx = -1
        min_val = 987654321
        for i in range(N+1):
            if not visited[i] and min_val > dist[i]:
                min_idx = i
                min_val = dist[i]
        visited[min_idx] = 1

        for i in range(N+1):
            if not visited[i] and dist[i] > dist[min_idx] + adj[min_idx][i]:
                dist[i] = dist[min_idx] + adj[min_idx][i]
    return dist

for tc in range(1, int(input()) + 1):
    N, M, X = map(int, input().split())  # N : 사람수, M : 간선수, X : 생일파티집
    INF = 100*N
    adj1 = [[INF] * (N + 1) for _ in range(N + 1)]  # 원래입력 (진출방향)
    adj2 = [[INF] * (N + 1) for _ in range(N + 1)]  # 뒤집은입력 (진입방향)

    for _ in range(M):
        x, y, c = map(int, input().split())  # c : 가중치
        adj1[x][y] = c
        adj2[y][x] = c

    dist1 = dijkstra(X, adj1)
    dist2 = dijkstra(X, adj2)

    max_value = -1

    for i in range(1, N+1):
        if dist1[i] + dist2[i] > max_value:
            max_value = dist1[i] + dist2[i]

    print('#{} {}'.format(tc, max_value))