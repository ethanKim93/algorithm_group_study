"""
bfs - 인접 행렬 or 인접 리스트 구현
방문한 node들 표시
"""
import sys
sys.stdin = open('input.txt')

# 인접 행렬
def bfs(s):      # s 시작 정점, V번 까지 존재
    global V
    q = []                  # 큐 생성
    visited = [0]*(V+1)     # visited 생성
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 시작점 visited 표시

    # 큐가 비어있지 않으면 (탐색할 node가 남아 있으면)
    while q:
        t = q.pop(0)                # t <- 디큐 (꺼내서)
        print(t)                    # t 처리
        for i in range(1, V+1):     # t에 인접하고, 미방문인 모든 i 찾아내기
            if adj[t][i] == 1 and visited[i] == 0:
                q.append(i)         # enqueue(i)
                visited[i] = visited[t] + 1      # i visited로 표시


# 인접 리스트
def bfs2(s):      # s 시작 정점, V번 까지 존재
    global V
    q = []                  # 큐 생성
    visited = [0]*(V+1)     # visited 생성
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 시작점 visited 표시

    # 큐가 비어있지 않으면 (탐색할 node가 남아 있으면)
    while q:
        t = q.pop(0)                # t <- 디큐 (꺼내서)
        print(t)                    # t 처리
        for i in adjList[t]:        # t에 인접하고, 미방문인 모든 i 찾아내기
            if visited[i] == 0:     # 인접 행렬과 달리 이미 방문 노드를 꺼내기 때문에 visited만 고려
                q.append(i)         # enqueue(i)
                visited[i] = visited[t] + 1      # i visited로 표시


# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
edge = list(map(int, input().split()))



# Graph 초기화(인접 행렬)
adj = [[0]*(V+1) for _ in range(V+1)]
# Graph 초기화(인접 리스트)
adjList = [[]]
for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    adjList.append([n1, n2])



# 방문 표시 초기화
for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1     # 방향이 없는 경우

# bfs 탐색 시작
bfs(1)
bfs2(1)





