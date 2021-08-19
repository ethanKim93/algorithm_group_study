import sys
sys.stdin = open('input.txt')

def dfs(v):  # v: 현재 방문하는 정점(스타트 지점)
    visited[v] = 1  # 들어오자마자 방문체크 1
    # 방문하지 않은 인접정점을 찾는다.
    for w in range(1, V + 1):
        if G[v][w] == 1 and not visited[w]:
            dfs(w)

V = 100
T = 10
for t in range(1, T+1):
    tc, E = map(int, input().split())
    matrix = list(map(int, input().split()))
    visited = [0] * (V)
    # 인접행렬
    G = [[0] * (V + 1) for _ in range(V + 1)]  # 0번은 안쓰고 1번부터 V까지 써야하니까/행.렬
    for _ in range(E):  # 간선의 개수만큼 들어온다
        u = matrix[2 * _]
        v = matrix[2 * _ + 1]
        G[u][v] = 1

    # for i in range(1, V + 1):
    #     print(i, '--->', G[1:])
    # print(matrix)
    # print(visited)
    dfs(0)
    ans = 0

    if visited[99]:
        ans = 1

    print('#{} {}'.format(tc, ans))