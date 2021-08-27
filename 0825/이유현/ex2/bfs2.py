"""
bfs - 인접 리스트 구현
"""
import sys
sys.stdin = open('input.txt')


def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        t = q.pop(0)
        print(t)
        for i in adjList[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1


# V(ertex), E(dge)
V, E = map(int, input().split())
# 간선 정보 초기화
edge = list(map(int, input().split()))
# Graph 초기화
adjList = [[] for _ in range(V+1)]

for i in range(0, E*2, 2):
    n1, n2 = edge[i], edge[i+1]
    adjList[n1].append(n2)
    adjList[n2].append(n1)

# 방문 표시 초기화
visited = [0] * (V+1)
# bfs 탐색 시작
bfs(1)