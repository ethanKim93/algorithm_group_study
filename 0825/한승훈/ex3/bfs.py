"""
bfs - 인접 행렬 or 인접 리스트 구현
"""


def bfs(v):
    queue.append(v)
    visited[v] = 1
    while queue:
        t = queue.pop(0)
        print(t)
        for i in range(1, V+1):
            if not visited[i] and G[t][i]:
                queue.append(i)
                visited[i] = visited[t] + 1
    pass


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
lst = list(map(int, input().split()))

# Graph 초기화
G = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    G[lst[2*i]][lst[2*i+1]] = G[lst[2*i+1]][lst[2*i]] = 1

# 방문 표시 초기화
visited = [0] * (V+1)
queue = []
# bfs 탐색 시작
bfs(1)