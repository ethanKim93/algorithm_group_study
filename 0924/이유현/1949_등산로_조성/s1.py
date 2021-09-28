import sys
sys.stdin = open('sample_input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dfs(r, c, cnt, cut):
    global ans
    if cnt > ans:
        ans = cnt
    visited[r][c] = 1
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if nr in range(N) and nc in range(N) and visited[nr][nc] != 1:
            if arr[nr][nc] < arr[r][c]:
                dfs(nr, nc, cnt+1, cut)

            elif cut and arr[nr][nc] - K < arr[r][c]:
                temp = arr[nr][nc]
                arr[nr][nc] = arr[r][c] - 1
                dfs(nr, nc, cnt+1, False)
                arr[nr][nc] = temp
    visited[r][c] = 0


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]

    maxV = 0
    for a in arr:
        for n in a:
            if n > maxV:
                maxV = n

    ans = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == maxV:
                dfs(r, c, 1, True)

    print('#{} {}'.format(tc, ans))