import sys
sys.stdin = open('sample_input.txt')

def dfs(i):
    global ans
    visited[i] = 1
    if visited.count(1) > ans:
        ans = visited.count(1)
    for x in link[i]:
        if visited[x] == 0:
            dfs(x)
            visited[x] = 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    link = [[] for _ in range(N+1)]

    for _ in range(M):
        x, y = map(int, input().split())
        link[x].append(y)
        link[y].append(x)

    ans = 0
    for i in range(1, N+1):
        visited = [0] * (N + 1)
        dfs(i)
    print('#{} {}'.format(tc, ans))