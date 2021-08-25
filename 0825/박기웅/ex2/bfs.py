"""
bfs - 인접 행렬 or 인접 리스트 구현
"""

# append, pop 으로 queue 구현

def bfs(v):
    q = []      # queue 생성
    q.append(v) # 시작점 enqueue
    visited[v] = 1 # visited 도장
    while q:            # q가 비어있지 않으면
        t = q.pop(0)    # dequeue 해서 t에 저장
        print(t)        # do something
        for i in range(V+1):  # 모든 정점 탐색
            if adj[t][i] and not visited[i]:    #인접해 있고 미방문이면
                visited[i] = visited[t] +1      # 방문 찍으면서 간선 거리 추가 갱신
                q.append(i)
                
# front, rear 로 queue 구현
def bfs2(v):
    q = [0]*(V+1)      # queue 생성
    front = rear = -1
    rear += 1
    q[rear] = v         # 시작점 enqueue
    visited[v] = 1
    while front != rear:    # q가 비어있지 않으면
        front += 1
        t = q[front]        # dequeue해서 t에 저장
        print(t)
        for i in range(V+1):
            if adj[t][i] and not visited[i]:
                visited[i] = visited[t] +1
                rear += 1
                q[rear] = i





import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())
# 간선 정보 초기화
edge = list(map(int, input().split()))
# Graph 초기화
# 인접 행렬
adj = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    adj[edge[2*i]][edge[2*i+1]] = 1
    adj[edge[2*i+1]][edge[2*i]] = 1     #무방향 그래프

# 인접 리스트
# adjList = [[] for _ in range(V+1)]
# for i in range(E):
#     adjList[edge[2*i]].append(edge[2*i+1])
#     adjList[edge[2*i+1]].append(edge[2*i])
# print(adjList)
# 방문 표시 초기화
visited = [0]*(V+1)
# bfs 탐색 시작
# bfs(1)
bfs2(1)