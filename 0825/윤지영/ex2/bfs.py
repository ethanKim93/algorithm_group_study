"""
bfs - 인접 행렬 or 인접 리스트 구현
"""

# 인접 리스트
def bfs(v):
    q = []          # 큐 생성
    q.append(v)     # 시작점 인큐 # enQ
    visited[v] = 1  # 시작점 visited
    while q:
        t = q.pop(0)    #deQ
        print(t)
        for w in adjList[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
edge = list(map(int, input().split()))

# Graph 초기화
adjList = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = edge[i*2], edge[i*2+1]
    adjList[n1].append(n2)

# 방문 표시 초기화
visited = [0] * (V+1)

# bfs 탐색 시작
bfs(1)

# 인접 행렬
# def bfs(v):
#     global V
#     q = []          # 큐 생성
#     q.append(v)     # 시작점 인큐    #enQ
#     visited[v] = 1  # 시작점 방문 표시
#     while q:
#         t = q.pop(0)    # q 디큐해서 t에 저장 #deQ
#         print(t)
#         for k in range(1, V+1):
#             if adj[t][k] == 1 and visited[k] == 0:  # 인접하고 미방문인 k에 대해
#                 q.append(k)                         # 인큐
#                 visited[k] = visited[t] + 1
#
#
# import sys
# sys.stdin = open('input.txt')
#
# # V(ertex), E(dge)
# V, E = map(int, input().split())
#
# # 간선 정보 초기화
# edge = list(map(int, input().split()))
#
# # Graph 초기화
# adj = [[0]*(V+1) for _ in range(V+1)]
# for i in range(V+1):
#     n1, n2 = edge[i*2], edge[i*2+1]
#     adj[n1][n2] = 1
#
# # 방문 표시 초기화
# visited = [0] * (V+1)
#
# # bfs 탐색 시작
# bfs(1)