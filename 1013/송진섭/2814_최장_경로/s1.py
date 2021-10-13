def dfs(v, cnt):
    global max_cnt
    visited[v] = 1
    if cnt > max_cnt:
        max_cnt = cnt
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w, cnt+1)
            visited[w] = 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj_list = [[] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    max_cnt = 1

    for i in range(M):
        x, y = map(int, input().split())
        adj_list[x].append(y)
        adj_list[y].append(x)
    for j in range(1, N+1):
        dfs(j, 1)
    print('#{} {}'.format(tc, max_cnt))
