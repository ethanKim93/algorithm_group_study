import sys
sys.stdin = open('input.txt')


# 스택으로 구현
def DFS(s):
    stack = []
    visited = [0] * (V+1)
    stack.append(s)
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            print(v)
            for w in adj_list[v]:
                stack.append(w)


V, E = map(int, input().split())
edges = list(map(int, input().split()))
adj_list = [[] for _ in range(V+1)]
for i in range(E):
    adj_list[edges[i*2]].append(edges[i*2+1])
    adj_list[edges[i*2+1]].append(edges[i*2])

DFS(1)