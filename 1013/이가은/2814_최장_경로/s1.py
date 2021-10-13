import sys
sys.stdin = open('sample_input.txt')

def dfs(i, cnt):
    global max_cnt

    for n in range(1, N+1):
        if not visited[n] and graph[i][n]:
            visited[n] = 1
            dfs(n, cnt + 1)
            visited[n] = 0
    else:
        if cnt > max_cnt:
            max_cnt = cnt


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[0]*(N+1) for _ in range(N+1)]
    visited = [0]*(N+1)
    max_cnt = 0
    for m in range(M):
        x, y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1
    for i in range(1, N+1):
        visited[i] = 1
        dfs(i,1)
        visited[i] = 0

    print('#{} {}'.format(tc,max_cnt))

