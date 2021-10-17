import sys
sys.stdin = open('input.txt')

def dijstra():
    dist = [987654321] * (V+1)
    visited = [0] * (V+1)

    dist[0] = 0

    for _ in range(V):
        min_idx = -1
        min_value = 987654321
        for i in range(V+1):
            if not visited[i] and min_value > dist[i]:
                min_idx = i
                min_value = dist[i]

        visited[min_idx] = 1
        for i in range(V+1):
            if not visited[i] and dist[i] > dist[min_idx] + adj_arr[min_idx][i]:
                dist[i] = dist[min_idx] + adj_arr[min_idx][i]
    print(dist)
    return dist[V]



T = int(input())

for tc in range(1, T+1):
    N, M, X = map(int, input().split())

    adj1 = [[987654321] * (N+1) for _ in range(N+1)]
    adj2 = [[987654321] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        x, y, c = map(int, input().split())
        adj1[x][y] = c
        adj2[y][x] = c

    dist1 = [987654321]* (N+1)
    dist2 = [987654321] * (N + 1)

    # 다익스트라 호출

    max_value = 0

    for i in range(1, N+1):
        if dist1[i] + dist2[i] > max_value:
            max_value = dist2[i] + dist2[i]

    print('#{} {}'.format(tc, max_value))
