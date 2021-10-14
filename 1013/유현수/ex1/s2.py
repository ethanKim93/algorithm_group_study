import sys
sys.stdin = open('input.txt')


def DFS_recursive(s):
    visited[s] = 1
    print(s)
    for w in adj_list[s]:
        if not visited[w]:
            DFS_recursive(w)


V, E = map(int, input().split())
edges = list(map(int, input().split()))
adj_list = [[] for _ in range(V+1)]
for i in range(E):
    adj_list[edges[i*2]].append(edges[i*2+1])
    adj_list[edges[i*2+1]].append(edges[i*2])

visited = [0] * (V+1)
DFS_recursive(1)