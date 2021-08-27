"""
bfs - 인접 행렬 or 인접 리스트 구현
"""

def bfs(v):
    q = [v]

    while q:
        v = q.pop(0)                                # 큐에서 확인하려는 정점 꺼냄
        if not visited[v]:
            visited[v] = 1                          # 현재 정점 방문 처리
            print(v, end=' ')                       # 현재 정점 출력
            for w in range(1, V+1):                 # 인접 행렬 구현시 정점 1~V 번을 순회하며 인접한 정점을 찾는다
                if adj[v][w] and not visited[w]:    # 인접했고 방문한 적이 없다면 큐에 추가
                    q.append(w)
            # for w in adjlist[v]:                  # 인접 리스트 구현시 현재 정점 v번 인덱스에 해당하는 리스트만 순회하면 된다
            #     if not visited[w]:                # 위에서 인접여부는 확인이 됐기 때문에 방문여부만 확인해서 큐에 추가
            #         q.append(w)


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
edges = list(map(int, input().split()))

# Graph 초기화(행렬 or 리스트 중 선택)
#1. 인접 행렬 초기화
adj = [[0] * (V+1) for _ in range(V+1)]

# 인접 행렬에 노드 별 인접 여부 행과 열을 바꾼 위치까지 기록(간선의 방향성이 없는 경우)
for i in range(E):
    adj[edges[i*2]][edges[i*2+1]] = 1
    adj[edges[i*2+1]][edges[i*2]] = 1

#2. 인접 리스트 초기화
# adjlist = [[] for _ in range(V+1)]

# 인접 리스트에 노드 별 인접 여부 기록
# for i in range(E):
#     adjlist[edges[i*2]].append(edges[i*2+1])

# 방문 표시 초기화
visited = [0] * (V+1)

# bfs 탐색 시작
bfs(1)