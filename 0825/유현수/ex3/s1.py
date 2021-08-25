"""
bfs - 인접 행렬 or 인접 리스트 구현
"""

def bfs(v):
    queue.append(v)
    visited[v] = 1
    while queue:
        curr = queue.pop(0)
        print(curr)
        for w in adj_list[curr]:
            if not visited[w]:
                queue.append(w)
                visited[w] = 1


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())
# 간선 정보 초기화
edges = list(map(int, input().split()))
adj_list = [[] for i in range(E+1)]
for i in range(E):
    adj_list[edges[2*i]].append(edges[2*i+1])
# Graph 초기화
queue = []
# 방문 표시 초기화
visited = [0] * (V+1)
# bfs 탐색 시작
bfs(1)
