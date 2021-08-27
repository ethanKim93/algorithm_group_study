"""
bfs - 인접 행렬 or 인접 리스트 구현
"""
# 인접 리스트
def bfs(v):
    q = [v]
    while q:
        v = q.pop(0)
        if not visited[v]:
            visited[v] = 1
            print(v, end = ' ')
            for w in range(1, V+1):
                if adj[v][w] and not visited[w]:
                    q.append(w)


# from pprint import pprint
import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
edges = list(map(int, input().split()))

# Graph 초기화
adj = [[0]*(V+1) for _ in range(V+1)]

for i in range(E):
    adj[edges[2*i]][edges[2*i+1]] = 1
    adj[edges[2 * i + 1]][edges[2 * i]] = 1
# pprint(adj)

# 방문 표시 초기화
visited = [0] * (V+1)

# bfs 탐색 시작
bfs(1)

################################################################### 인접 행렬
def bfs2(v):
    q = [v]
    while q:
        v = q.pop(0)
        if not visited[v]:
            visited[v] = 1
            print(v, end = ' ')
            for w in adjlist[v]:
                if not visited[w]:
                    q.append(w)

adjlist = [[] for _ in range(V+1)]

for i in range(E):
    adjlist[edges[i*2]].append(edges[i*2+1])

bfs2(1)