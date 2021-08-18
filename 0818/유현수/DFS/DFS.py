def dfs(s, V):              # s는 시작 정점, V는 정점의 개수
    visited = [0]*(V+1)
    stack = []
    i = s                   # 현재 방문한 정점 i
    visited[i] = 1
    print(node[i])
    while i != 0:
        for w in range(1, V+1):
            if adj[i][w] == 1 and visited[w] == 0:
                stack.append(i)
                i = w
                visited[i] = 1
                print(node[i])
                break
        else:
            if stack:
                i = stack.pop()
            else:
                i = 0


#          A  B  C  D  E  F  G
adj = [[0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 0, 0], # A
       [0, 1, 0, 0, 1, 1, 0, 0], # B
       [0, 1, 0, 0, 0, 1, 0, 0], # C
       [0, 0, 1, 0, 0, 0, 1, 0], # D
       [0, 0, 1, 1, 0, 0, 1, 0], # E
       [0, 0, 0, 0, 1, 1, 0, 1], # F
       [0, 0, 0, 0, 0, 0, 1, 0]] # G
node = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

dfs(1, 7)

"""
입력
7, 8    => 정점, 간선의 개수
1, 2    => 정점 1과 2가 인접
1, 3    => 정점 1과 3이 인접
...

V, E = map(int, input().split())
ad = [[0] * (V+1) for _ in range(V+1)]
for _ in range(E):
    n1, n2 = map(int, input().split())
    ad[n1][n2] = 1
    ad[n2][n1] = 1


출력
           A  B  C  D  E  F  G
adj = [[0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 0, 0],  A
       [0, 1, 0, 0, 1, 1, 0, 0],  B
       [0, 1, 0, 0, 0, 1, 0, 0],  C
       [0, 0, 1, 0, 0, 0, 1, 0],  D
       [0, 0, 1, 1, 0, 0, 1, 0],  E
       [0, 0, 0, 0, 1, 1, 0, 1],  F
       [0, 0, 0, 0, 0, 0, 1, 0]]  G
"""