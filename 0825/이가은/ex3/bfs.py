"""
bfs - 인접 행렬 or 인접 리스트 구현
"""

def bfs(v):
    '''
    q = [v]

    while q:
        t = q.pop(0)

        if not visited[t]:
            visited[t] = 1
            print(t, end = ' ')

            for i in range(1, V+1):
                if graph[t][i] and not visited[i]:
                    q.append(i)
    '''
    q = [v]

    while q:
        t = q.pop(0)

        if not visited[t]:
            visited[t] = 1
            print(t, end = ' ')

            for i in graph_li[t]:
                if not visited[i]:
                    q.append(i)


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
edge = list(map(int, input().split()))
edge_li = list([] for _ in range(V+1))

# Graph 초기화
# graph = [[0]*(V+1) for _ in range(V+1)]
graph_li = [[] for _ in range(V+1)]

# for i in range(E):
#     n1, n2 = edge[2*i], edge[2*i+1]
#     graph[n1][n2] = 1
#     graph[n2][n1] = 1
for i in range(E):
    graph_li[edge[2*i]].append(edge[2*i+1])
print(graph_li)


# 방문 표시 초기화
visited = [0] * (V+1)

# bfs 탐색 시작
print(bfs(1))