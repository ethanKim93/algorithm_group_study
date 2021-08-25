"""
bfs - 인접 행렬 or 인접 리스트 구현
"""

import sys
sys.stdin = open('input.txt')


# append, pop 으로 queue 구현

def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        t = q.pop(0)
        print(t)
        for i in range(V + 1):
            if lst[t][i] and not visited[i]:
                visited[i] = visited[t] + 1
                q.append(i)


# V(ertex), E(dge)
V, E = map(int, input().split())
# 간선 정보 초기화
edge = list(map(int, input().split()))
# Graph 초기화
lst = []
for k in range(V + 1):
    lst.append([0] * (V + 1))
for j in range(E):
    lst[edge[2 * j]][edge[2 * j + 1]] = 1
    lst[edge[2 * j + 1]][edge[2 * j]] = 1
# 방문 표시 초기화
visited = [0] * (V + 1)
# bfs 탐색 시작
bfs(1)
