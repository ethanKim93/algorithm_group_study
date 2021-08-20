def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, V+1):
        if G[v][i] == 1 and visit[i] == 0:  # 간선으로 연결되어 있고 방문을 안했다면 dfs
            dfs(i)


V, E = 7, 8
temp = list(map(int, input().split()))

# 간선을 넣는 곳(2차원)
G = [[0]*(V+1) for _ in range(V+1)]

# 방문을 체크해 주는 곳
visit = [0 for _ in range(V+1)]

for i in range(0, len(temp), 2):  # 1 2 가 들어오면 1, 2와 2, 1 둘다 체크한다
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1
# 1에서 시작하기 때문에 1 대입
dfs(1)
