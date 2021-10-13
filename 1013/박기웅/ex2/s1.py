'너비 우선탐색하여 경로를 출력하시오.'
edge = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
edge = list(map(int, edge.split()))
# 전체 노드 번호
V = list(range(1,8))
# 노드의 수
N = len(V)
# 인접행렬 정의
adjM = [[0]*(N+1) for _ in range(N+1)]
for i in range(len(edge)//2):
    n1, n2 = edge[2*i], edge[2*i+1]
    # 무방향 그래프로 인접행렬 초기화
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1

#선형 큐 활용 너비 우선탐색

Q = [0]*(N+1)
visited = [0]*(N+1)
front = rear = -1
#시작 정점을 1로 시작
# enqueue
rear += 1
Q[rear] = 1
while front != rear:
    # dequeue
    front += 1
    v = Q[front]
    visited[v] = 1
    print(v, end=' ')
    for n in range(1, N+1):
        if adjM[v][n] and not visited[n]:
            rear += 1
            Q[rear] = n
            visited[n] = 1

