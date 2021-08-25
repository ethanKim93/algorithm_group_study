"""
bfs - 인접 행렬 or 인접 리스트 구현
"""

def bfs(v):
    queue = []
    queue.append(v)         # queue = [v]
    visited[v] = 1
    while queue:
        t = queue.pop()         # t = queue.pop(0)
        print(t, end = ' ')
        for i in range(1, V+1):
            if adj[t][i] == 1 and visited[i] == 0:      # if adj[t][i] and not visited[i]
                queue.append(i)
                visited[i] = visited[t] + 1

# for i in adjList[t]:                      #인접리스트구현시
#    if visited[i] == 0:
#        queue.append(i)
#        visited[i] = visited[t] + 1

    # q = [0] * V
    # front = -1
    # rear = -1
    # rear += v       # 시작점 enque
    # q[rear] = v
    # visited[v] = 1
    # while front != rear:
    #     front += 1
    #     t = q[front]
    #     print(t, end = ' ')
    #     for i in range(1, V+1):
    #         if adj[t][i] == 1 and visited[i] == 0:
    #             rear += 1
    #             q[rear] = i
    #             visited[i] = visited[t] + 1

import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())
# 간선 정보 초기화
line = list(map(int, input().split()))
# Graph 초기화
adj = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    n1, n2 = line[2*i], line[2*i+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1

# adjList = []                          #인접리스트구현시
# n1, n2 = line[2*i], line[2*i+1]
# adjList[n1].append(n2)
# adjList[n2].append(n1)

# 방문 표시 초기화
visited = [0] * (V+1)
# bfs 탐색 시작
bfs(1)