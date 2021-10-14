import sys
sys.stdin = open('input.txt')


def DFS(s, cnt):
    global ans
    visited[s] = 1
    if ans < cnt:
        ans = cnt
    for w in adj[s]:
        if not visited[w]:
            DFS(w, cnt+1)
            visited[w] = 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)

    ans = 0
    for i in range(1, N+1):
        visited = [0] * (N+1)
        DFS(i, 1)

    print('#{} {}'.format(tc, ans))

