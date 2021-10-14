'깊이 우선탐색하여 경로를 출력하시오.'
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

#stack 활용 깊이 우선탐색
#시작 정점을 1로 시작
stack = [1]
# 각 노드의 방문 여부를 정의할 리스트
visited = [0]*(N+1)
print('STACK 1:', end =' ')
while stack:
    v = stack.pop()
    if not visited[v]:
        print(v, end =' ')
        visited[v] = 1
        for n in range(1, N+1):
            if adjM[v][n] and not visited[n]:
                stack.append(n)
print()

#stack 활용 깊이 우선탐색 
# push 할 때 방문 찍고 가기
visited = [0]*(N+1)
stack = [1]
visited[1] = 1
print('STACK 2:', end =' ')
while stack:
    v = stack.pop()
    print(v, end =' ')
    for n in range(1, N+1):
        if adjM[v][n] and not visited[n]:
            stack.append(n)
            visited[n] = 1
print()

#재귀 활용 깊이 우선탐색
visited = [0]*(N+1)
print('RECURSIVE:', end =' ')
def dfs(v):
    print(v, end=' ')
    visited[v] = 1
    for n in range(1, N+1):
        if adjM[v][n] and not visited[n]:
            dfs(n)
dfs(1)
print()

