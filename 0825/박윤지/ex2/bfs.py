"""
bfs - 인접 행렬 or 인접 리스트 구현
"""

def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        t = q.pop(0)
        print(t)
        for i in range(1, V+1):
            if visited[i] == 0 and graph[t][i] == 1:
                q.append(i)
                visited[i] = visited[t] + 1


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
edge = list(map(int, input().split()))

# Graph 초기화
graph = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    s, e = edge[i*2], edge[i*2 + 1]
    graph[s][e] = 1
    graph[e][s] = 1

# 방문 표시 초기화
visited = [0]*(V+1)

# bfs 탐색 시작
bfs(1)