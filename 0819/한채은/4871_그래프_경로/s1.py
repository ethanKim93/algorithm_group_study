import sys
sys.stdin = open("sample_input.txt")

T = int(input())


def dfs(v):  # v: 현재 방문하는 정점
    visited[v] = 1

    # 방문하지 않은 인접정점을 찾는다.

    for w in range(1, V + 1):
        if G[v][w] == 1 and not visited[w]:
            dfs(w)


for tc in range(1, T+1):
    V, E = map(int, input().split())  # 정점수, 간선수

    # 인접 행렬렬
    G = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0 for _ in range(V + 1)]  # 노드가 지나는지

    for _ in range(E):
        u, v = map(int, input().split())
        G[u][v] = 1     # 단방향이기 때문에 G[v][u]는 없음

    S, E = map(int, input().split())
    dfs(S)
    print('#{} {}'.format(tc, visited[E]))



