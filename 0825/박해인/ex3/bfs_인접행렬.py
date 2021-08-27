"""
bfs - 인접 행렬 or 인접 리스트 구현
"""

# def bfs(s, V):
#     q = []
#     visited = [0] * (V+1)
#     q.append(s)
#     visited[s] = 1
#
#     while q:  # 처리할 정점이 남아있다면
#         t = q.pop(0)
#         print(t)
#         for i in range(1, V+1):
#             if adj[t][i] == 1 and visited[i] == 0:
#                 q.append(i)
#                 visited[i] = 1

def bfs(v):
    q = [v]

    while q:  # 처리할 정점이 남아있다면
        v = q.pop(0)
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            for w in range(1, V+1):
                adj[v][w] and not visited[w]:
                    q.append(w)


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())
# 간선 정보 초기화
edge = list(map(int, input().split()))
# Graph 초기화
adj = [[0] * (V+1) for _ in range(V+1)]

for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1
# 방문 표시 초기화
visited = [0] * (V+1)
# bfs 탐색 시작
bfs(1)