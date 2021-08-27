"""
bfs - 인접 행렬 or 인접 리스트 구현
"""

def bfs(s): #인접 행렬
    q = [s]
    visited = [0] * (V+1)
    visited[s] = 1

    while q:
        t = q.pop(0)
        print(t, end="-")
        for i in range(1,V+1):
            if adj[t][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1
    print('인접 행렬 탐색 끝')

def bfs2(s):
    q = [s]
    visited = [0] * (V+1)
    visited[s] = 1

    while q:
        t = q.pop(0)
        print(t, end="-")
        for i in adj_list[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1
    print("인접 리스트 탐색 끝")

import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
line = list(map(int, input().split()))

# Graph 초기화
adj = [[0]*(V+1) for _ in range(V+1)]
adj_list = [[] for _ in range(V+1)]

# 방문 표시 초기화
for i in range(V+1):
    n1, n2 = line[2*i], line[2*i+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1

    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

# bfs 탐색 시작
bfs(1)
bfs2(1)