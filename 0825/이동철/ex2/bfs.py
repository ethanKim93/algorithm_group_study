"""
bfs - 인접 행렬 or 인접 리스트 구현
"""


def bfs1(s, V):
    q = []  # Queue 생성
    visited = [0] * (V + 1) # visited 생성
    q.append(s) # 시작점 enQueue
    visited[s] = 1  # 시작점 visited 표시
    while q:    # Queue가 비어있지 않으면 (처리할 정점이 )
        t = q.pop(0) # deQueue, 꺼내서 t에 저장
        print(t)    # t에 대한 처리
        for i in range(1, V + 1):   # t에 인접이고 미방문
            if adj[t][i] == 1 and visited[i] == 0:
                q.append(i) # enQueue(i)
                visited[i] = visited[t] + 1 # i visited로 표시


def bfs2(s, V):
    q = []  # Queue 생성
    visited = [0] * (V + 1) # visited 생성
    q.append(s) # 시작점 enQueue
    visited[s] = 1  # 시작점 visited 표시
    while q:    # Queue가 비어있지 않으면 (처리할 정점이 )
        t = q.pop(0) # deQueue, 꺼내서 t에 저장
        print(t)    # t에 대한 처리
        for i in adj_lst[t]:   # t에 인접이고 미방문
            if visited[i] == 0:
                q.append(i) # enQueue(i)
                visited[i] = visited[t] + 1 # i visited로 표시


import sys
sys.stdin = open('input.txt')


V, E = map(int, input().split())    # V(ertex), E(dge)

edge = list(map(int, input().split()))  # 간선 정보 초기화
# 1. Graph 초기화 # 인접행렬 이용
adj = [[0] * (V + 1) for _ in range(V + 1)]
# 2. 인접리스트 이용
adj_lst = [[] for _ in range(V + 1)]

for i in range(E):
    n1, n2 = edge[2 * i], edge[2 * i + 1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1 #방향이 없는 그래프

    adj_lst[n1].append(n2)
    adj_lst[n2].append(n1)

# 방문 표시 초기화
# visited = [0] * (V + 1)

# bfs 탐색 시작
bfs1(1, V)
bfs2(1, V)