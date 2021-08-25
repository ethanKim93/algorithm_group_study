"""
bfs - 인접 행렬 or 인접 리스트 구현
"""


def bfs(v):
    queue = [v]
    visited[v] = 1

    while queue:
        t = queue.pop(0)
        print(t)
        for i in range(1, len(adj)):
            if adj[t][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1  # visited[i] += 1


def bfs2(v):
    queue = [v]
    visited[v] = 1

    while queue:
        t = queue.pop(0)
        print(t)
        for i in adj_list[t]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1  # visited[i] += 1


def bfs3(v):
    queue = []
    front = rear = -1  # enqueue(v)
    queue.append(v)
    rear += 1
    visited[v] = 1

    while front != rear:
        front += 1
        t = queue[front]  # dequeue()
        print(t)
        for i in adj_list[t]:
            if visited[i] == 0:
                rear += 1  # enqueue(i)
                queue.append(i)
                visited[i] = 1  # visited[i] += 1


import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())  # V(ertex), E(dge)
edge_list = list(map(int, input().split()))  # 간선 정보 초기화
adj = [[0] * (V+1) for _ in range(V+1)]  # Graph 초기화
adj_list = [[] for _ in range(V+1)]

for i in range(E):
    adj[edge_list[i*2]][edge_list[i*2+1]] = 1
    adj[edge_list[i*2+1]][edge_list[i*2]] = 1
    adj_list[edge_list[i*2]].append(edge_list[i*2+1])
    adj_list[edge_list[i*2+1]].append(edge_list[i*2])

visited = [0] * (V+1)  # 방문 표시 초기화

# bfs 탐색 시작
bfs3(1)