import sys
sys.stdin = open('input.txt')


def BFS(s):
    Q = []
    Q.append(s)
    visited[s] = 1
    print(s)
    while Q:
        t = Q.pop(0)
        for w in adj_list[t]:
            if not visited[w]:
                Q.append(w)
                visited[w] = 1
                print(w)


V, E = map(int, input().split())
edges = list(map(int, input().split()))
adj_list = [[] for _ in range(V+1)]
for i in range(E):
    adj_list[edges[i*2]].append(edges[i*2+1])
    adj_list[edges[i*2+1]].append(edges[i*2])
visited = [0] * (V+1)
BFS(1)