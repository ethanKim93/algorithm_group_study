"""
bfs - 인접 행렬 or 인접 리스트 구현
"""

def bfs(v):
    queue.append(v)
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = 1
            print(t+1)
            for i in range(len(edges[t])):
                if visited[edges[t][i]] != 1:
                    queue.append(edges[t][i])

import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())
Es = list(map(int, input().split()))
# 간선 정보 초기화
edges = [[] for _ in range(V)]
# Graph 초기화
for i in range(E):
    edges[Es[2*i]-1].append(Es[2*i + 1]-1)
    edges[(Es[2*i + 1]-1)].append(Es[2*i]-1)
# 방문 표시 초기화
visited = [0] * V
queue = []
# bfs 탐색 시작
bfs(0)