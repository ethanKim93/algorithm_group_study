import sys
sys.stdin = open('sample_input.txt')
import time
start = time.time()


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adj = [[0] * (N + 1) for _ in range(N + 1)]
    inf = 1000
    visited = [0] * (N + 1)
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w  # 방향 o
    key = [inf] * (N+1)
    key[0] = 0
    for _ in range(N):
        u = 0
        minV = inf
        for i in range(N+1):
            if not visited[i] and key[i] < minV:
                u = i
                minV = key[i]
        visited[u] = 1

        if u == N:
            break
        for v in range(N+1):
            if not visited[v] and adj[u][v]:
                if key[v] > key[u] + adj[u][v]:
                    key[v] = adj[u][v] + key[u]

    print('#{} {}'.format(tc, key[N]))


print("time :", time.time() - start)