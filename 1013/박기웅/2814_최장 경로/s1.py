# import sys
# sys.stdin = open('sample_input.txt')

def dfs(s, r):
    global max_route
    max_route = max(max_route, r)
    for w in range(1, N+1):
        if adjM[s][w] and not visited[w]:
            visited[w] = 1
            dfs(w, r+1)
            visited[w] = 0  # 나올 때 다른 경로 탐색할 수 있도록 방문 풀어주기
    

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 인접 배열 정의
    adjM = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        # 무방향 그래프
        adjM[a][b] = 1
        adjM[b][a] = 1

    max_route = 0
    for i in range(1, N+1):
        visited = [0]*(N+1)
        visited[i] = 1  # 방문하고 들어가기
        dfs(i, 1)
    
    print('#{} {}'.format(tc, max_route))

    
