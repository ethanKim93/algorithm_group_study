import sys
sys.stdin = open('sample_input.txt', 'r')


def dfs(idx, cnt):
    global max_cnt

    visit[idx] = True

    if cnt > max_cnt:
        max_cnt = cnt

    for i in adj[idx]:
        if not visit[i]:
            dfs(i, cnt+1)
            visit[i] = 0


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    adj = [[] for i in range(n+1)]
    for i in range(m):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)

    max_cnt = 0
    for i in range(1, n+1):
        visit = [0] * (n+1)
        dfs(i, 1)
    print('#{} {}'.format(tc, max_cnt))
