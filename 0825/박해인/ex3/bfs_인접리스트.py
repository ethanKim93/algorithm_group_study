"""
bfs - 인접 행렬 or 인접 리스트 구현
"""
def bfs(v):
    q = [v]

    while q:  # 처리할 정점이 남아있다면
        v = q.pop(0)
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            for w in adjList[v]:
                if not visited[w]:
                    q.append(w)


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())
# 간선 정보 초기화
edge = list(map(int, input().split()))
# Graph 초기화
adjList = [[] for _ in range(V+1)]

for i in range(E):
    adjList[edge[i*2]].append(edge[i*2+1])
print(adjList)
# 방문 표시 초기화
visited = [0] * (V+1)
# bfs 탐색 시작
bfs(1)