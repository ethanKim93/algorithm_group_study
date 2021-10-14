import sys
sys.stdin = open('input.txt')

def dfs(v, cnt):
    global ans
    if cnt > ans:
        ans = cnt

    for i in range(1, N+1):
        if adj[v][i] and not visitied[i]:
            visitied[i] = 1
            dfs(i, cnt+1)
            visitied[i] = 0

for tc in range(1, int(input())+1):
    ans = 0
    N, M = map(int, input().split())
    adj = [[0]*(N+1) for _ in range(N+1)]
    visitied = [0] * (N + 1)
    for i in range(M):
        a, b = map(int, input().split())
        adj[a][b] = 1
        adj[b][a] = 1

    for i in range(1, N+1):
        if not visitied[i]:
            visitied[i] = 1
            dfs(i, 1)
            visitied[i] = 0
    print('#{} {}'.format(tc, ans))