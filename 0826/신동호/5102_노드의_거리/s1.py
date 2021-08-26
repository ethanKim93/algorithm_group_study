import sys
sys.stdin = open('sample_input.txt')

def dfs(v, dist):
    q = [v] # q에 v 넣기
    while q: # q에 값이 있는 동안
        v = q.pop(0) # dequeue
        visited[v] = dist # 거리를 visited에 넣어줌
        for w in range(1, V+1): # 모든 노드 v개에 대해
            if adj[v][w] and not visited[w]: # w가 연결되어 있고, visited가 0인 경우
                dfs(w, dist + 1) # w로 거리 1 늘려서 시작
            elif adj[v][w] and visited[w] > (dist + 1): # w가 연결되어 있고, 지금 거리 dist + 1이 기존의 거리 visited[w] 보다 작은 경우 (visited[w]가 방문하지 않았단 뜻의 0인 경우는 위에서 제거)
                dfs(w, dist + 1)




T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    visited = [0] * (V+1)
    edges = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)] # 인접 리스트 만들기
    dist = 0 # 거리 0으로 시작
    for i in range(E): # 인접 리스트 양방향으로 채우기
        adj[edges[i][0]][edges[i][1]] = 1
        adj[edges[i][1]][edges[i][0]] = 1
    dfs(S, dist)
    print('#{} {}'.format(tc, visited[G]))