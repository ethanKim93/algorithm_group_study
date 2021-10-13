import sys
sys.stdin = open('sample_input.txt')
def dfs(i, cnt):
    global maxV

    for j in range(1, N+1):
        if not visited[j] and arr[i][j]:
            visited[j] = 1
            dfs(j, cnt+1)
            visited[j] = 0
        else:
            if cnt > maxV:
                maxV = cnt



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    visited = [0] * (N+1)
    maxV = 0

    for _ in range(M):
        x, y = map(int, input().split())
        arr[x][y] = 1
        arr[y][x] = 1

    for i in range(1, N+1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0

    print('#{} {}'.format(tc, maxV))
