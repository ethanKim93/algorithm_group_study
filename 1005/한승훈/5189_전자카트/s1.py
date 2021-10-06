import sys
sys.stdin = open('sample_input.txt')


def dfs(u, cnt, ans):
    global result
    if ans > result:
        return

    if cnt == N-1:
        ans += matrix[u][0]  # 사무실로 백
        if ans < result:
            result = ans
        return

    for z in range(1, N):
        if not visited[z] and matrix[u][z]:
            visited[z] = 1
            dfs(z, cnt+1, ans + matrix[u][z])
            visited[z] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    result = 10000
    dfs(0, 0, 0)
    print('#{} {}'.format(tc, result))

