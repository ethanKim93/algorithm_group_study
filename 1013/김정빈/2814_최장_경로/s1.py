import sys
sys.stdin = open("input.txt")
#2814. 최장 경로
def dfs(s, cnt):
    global res
    visited[s] = 1
    for i in range(N+1):
        if adj[s][i] and not visited[i]:
            dfs(i, cnt+1)
    else:
        if res < cnt:
            res = cnt
        visited[s] = 0
        return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj = [[0]*(N+1) for _ in range(N+1)]
    visited = [0]*(N+1)
    res = 0
    for _ in range(M):
        x, y = map(int, input().split())
        adj[x][y] = 1
        adj[y][x] = 1
    for i in range(1, N+1):
        dfs(i, 1)

    print('#{} {}'.format(tc, res))