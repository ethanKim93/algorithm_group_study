"""
input
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

output
1-2-4-6-5-7-3
1-3-7-6-5-2-4
"""
def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for w in range(1, V+1):
        if adjM[v][w] == 1 and not visited[w]:
            dfs(w)

V, E = map(int, input().split())
edges = list(map(int, input().split()))
adjM = [[0] * (V+1) for _ in range(V+1)]
visited = [0] * (V+1)

for i in range(E):
    s, e = edges[2*i], edges[(2*i)+1]
    adjM[s][e] = 1
    adjM[e][s] = 1

dfs(1)