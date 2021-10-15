import sys
sys.stdin = open('sample_input.txt', 'r')


def dijkstar(s):
    visited = [0] * (N + 1)
    visited[s] = 1

    for i in range(N + 1):
        if adj[s][i]:
            price[i] = adj[s][i]

    for j in range(N):
        u = 0
        min_v = num
        for k in range(N + 1):
            if not visited[k] and price[k] < min_v:
                min_v = price[k]
                u = k
        visited[u] = 1

        for l in range(N + 1):
            if 0 < adj[u][l] < num:
                price[l] = min(price[l], price[u] + adj[u][l])

    return price[N]


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    # N은 마지막 연결지점 번호, E는 도로의 개수
    adj = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    # 노드와 거리 표현을 위한 2차원 list
    for _ in range(E):
        s_node, e_node, w = map(int, input().split())
        adj[s_node][e_node] = w
        # 방향 O

    num = 987654321
    price = [num] * (N + 1)
    dijkstar(0)
    print('#{} {}'.format(tc, price[N]))
