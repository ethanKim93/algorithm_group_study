import sys
sys.stdin = open('input.txt')


def dijkstra(start, lst):
    U = [0] * (N + 1)  # 사용된 정점
    dist = [987654321]*(N+1)
    dist[start] = 0

    for i in range(N):
        min_idx = -1
        min_value = 99999
        for i in range(N + 1):
            if U[i] == 0 and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]
        U[min_idx] = 1

        for j in range(N+1):
            if lst[min_idx][j] != 987654321:
                if dist[j] > dist[min_idx] + lst[min_idx][j]:
                    dist[j] = dist[min_idx] + lst[min_idx][j]

    return dist


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())

    go = [[987654321]*(N+1) for _ in range(N+1)]
    back = [[987654321] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        x, y, c = map(int, input().split())
        go[x][y] = c
        back[y][x] = c      # 결국 x->2 로 돌아가는 그래프 == i,j 반전한 그래프에서 2->x

    go_time = dijkstra(X, go)
    back_time = dijkstra(X, back)

    time = 0
    for i in range(1, N+1):
        if i != X and go_time[i] + back_time[i] > time:
            time = go_time[i] + back_time[i]

    print('#{} {}'.format(tc, time))