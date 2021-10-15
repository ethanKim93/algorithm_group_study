import sys
sys.stdin = open('input.txt', 'r')


def dijkstra(n, dist, adj):
    visited = [0] * (N + 1)
    visited[n] = 1
    for k in range(N + 1):
        dist[k] = adj[n][k]
    for _ in range(N):
        w = 0
        min_value = 987654321
        for l in range(1, N + 1):
            if visited[l] == 0 and min_value > dist[l]:
                w = l
                min_value = dist[l]
        visited[w] = 1
        for m in range(1, N + 1):
            if 0 < adj[w][m] < 987654321:
                dist[m] = min(dist[m], dist[w] + adj[w][m])


T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    # N 은 사람 수, M 은 간선 수, X 는 생일 파티 집

    adj1 = [[987654321] * (N + 1) for _ in range(N + 1)]
    # 원래 입력(진출)
    adj2 = [[987654321] * (N + 1) for _ in range(N + 1)]
    # 뒤집은 입력(진입)

    for _ in range(M):
        x, y, c = map(int, input().split())
        # c 는 가중치
        adj1[x][y] = c
        adj2[y][x] = c

    dist1 = [987654321] * (N + 1)
    dist2 = [987654321] * (N + 1)

    for j in range(N + 1):
        adj1[j][j] = 0
        adj2[j][j] = 0

    dijkstra(X, dist1, adj1)
    # X번 까지 가는길
    dijkstra(X, dist2, adj2)
    # X번 에서 돌아오는길

    max_value = 0
    for i in range(1, N + 1):
        if dist1[i] + dist2[i] > max_value:
            max_value = dist1[i] + dist2[i]

    print('#{} {}'.format(tc, max_value))


