def bfs(v):
    q = [v]

    while q:
        v = q.pop()
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            for w in range(1, V+1):
                if adj[v][w] and not visited[w]:
                    q.append(w)


import sys
sys.stdin = open('input.txt')

V, E = 7, 7
edges = list(map(int, input().split()))
adj = [[0] * (V+1) for _ in range(V+1)]

for i in range(E):
    adj[edges[i*2]][edges[i*2+1]] = 1
    adj[edges[i*2+1]][edges[i*2]] = 1

visited = [0] * (V+1)

bfs(1)
