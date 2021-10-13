'''
마지막 정점번호, 간선 수
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

V, E = map(int, input().split())
edge = list(map(int, input().split()))

adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)
print(adjL)


def DFS(s, V):
    stack = []
    visited = [0] * (V + 1)
    stack.append(s)
    visited[s] = True
    while stack:
        t = stack.pop()
        print(t)
        for i in adjL[t]:
            if visited[i] == 0:
                stack.append(i)
                visited[i] = True


DFS(1, V)