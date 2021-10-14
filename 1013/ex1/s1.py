'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def DFS(s):
    stack = []
    visited = [0] * (V+1)
    stack.append(s)
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            print(v)
            for j in adj[v]:
                stack.append(j)


V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[] for _ in range(V+1)]
for i in range(E):
    adj[edge[i*2]].append(edge[i*2+1])
    adj[edge[i*2+1]].append(edge[i*2])
DFS(1)