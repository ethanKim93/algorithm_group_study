import sys
sys.stdin = open('sample_input.txt')

def bfs(S, G):
    q = []
    visited = [0] * (V+1)
    q.append(S)

    while q:
        t = q.pop(0)
        for i in range(1, V+1):
            if adj[t][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1    # 거쳐온 거리 + 1 = 현재까지의 거리
                if i == G:
                    return visited[i]  # 직전 노드의 visited 값을 return

    return 0

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    adj = [[0]*(V+1) for _ in range(V+1)]

    # print(edges)
    for i in range(E):
        n1, n2 = edges[i][0], edges[i][1]
        adj[n1][n2] = 1
        adj[n2][n1] = 1

    S, G = map(int, input().split())

    # bfs(S, G)
    print('#{} {}'.format(test_case, bfs(S, G)))
    # 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지

