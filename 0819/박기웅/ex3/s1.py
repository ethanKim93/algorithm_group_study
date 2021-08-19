from pprint import pprint
V = 7 #정점 개수
#간선 E
E = [(1, 2), (1, 3), (2, 4), (2, 5), (4, 6), (5, 6), (6, 7), (3, 7)]
#인접행렬
adj = [[0]*(V+1) for _ in range(V+1)]

for _ in range(len(E)):
    n1, n2 = E[_]
    adj[n1][n2] = 1
    adj[n2][n1] = 1

pprint(adj)

def dfs(s, V):
    visited = [0]*(V+1)
    stack = []
    i = s               # 현재 방문한 정점 i
    visited[i] = 1      # 방문한 경우 0->1
    print("탐색 경로: {}".format(node[i]),end = " ")
    while i:            # 스택에 저장된 게 없으면 i=0
        for w in range(1, V+1):
            if adj[i][w] and visited[w] == 0:    # 인접한데 방문하지 않은 곳이 있으면 
                stack.append(i)                  # 방문 경로 저장
                i = w                            # 새 방문지 이동
                visited[w] = 1                   # 방문한 노드로 저장
                print(node[i], end = " ")
                break
        else:                   # 더이상 갈 곳이 없는 경우
            if stack:
                i = stack.pop() # 스택에 최근 갔던 곳으로 돌아가서 다시 찾기
            else:
                i = 0           # 스택에 저장된 게 없으면 루프 종료

node = [0, 1, 2, 3 , 4, 5, 6, 7]    
dfs(1, 7)
