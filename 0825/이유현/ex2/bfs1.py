"""
bfs - 인접 행렬 구현
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
        for i in range(1, V+1):
            if adj[t][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1


# V(ertex), E(dge)
V, E = map(int, input().split())
# 간선 정보 초기화
edge = list(map(int, input().split()))
# Graph 초기화
adj = [[0]*(V+1) for _ in range(V+1)]
for i in range(0, E*2, 2):
    n1, n2 = edge[i], edge[i+1]

    adj[n1][n2] = 1
    adj[n2][n1] = 1
print(adj)
# 방문 표시 초기화
visited = [0] * (V + 1)
# bfs 탐색 시작
bfs(1)