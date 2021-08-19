import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split()) # 정점수, 간선수
# 인접 리스트
# G = [[] for _ in range(V + 1)]
# for _ in range(E):
#     u, v = map(int, input().split())
#     G[u].append(v)
#     G[v].append(u)
#
# for i in range(1, V + 1):
#     print(i, '-->', G[i])

# 인접 행렬
G = [[0] * (V+1) for _ in range(V+1)]
for _ in range(E):
    u, v = map(int, input().split())
    G[u][v] = G[v][u] = 1

visited = [0] * (V+1)

def dfs(v):     # v: 현재 방문하는 정점
    visited[v] = 1
    print(v, end=' ')
    # 방문하지 않은 인접정점을 찾는다.
    for w in range(1, V+1):
        if G[v][w] == 1 and not visited[w]:
            dfs(w)

dfs(1)