import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(idx, ans):
    global answer
    visited[idx] = 1
    ans += 1
    if answer < ans:
        answer = ans
    for i in graph[idx]:
        if not visited[i]:
            dfs(i, ans)
    visited[idx] = 0


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = (N+1)*[0]
    temp = [list(map(int, input().split())) for i in range(M)]
    graph = [[] for i in range(N + 1)]
    answer = 0

    for a, b, in temp:
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, N+1):
        dfs(i, 0)
    print('#{} {}'.format(tc, answer))