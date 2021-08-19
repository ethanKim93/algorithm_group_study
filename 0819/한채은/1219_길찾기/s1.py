import sys
sys.stdin = open("input.txt")


def dfs(v):
    visited[v] = 1
    for w in range(1, v+1):
        if G[v][w] == 1 and not visited[w]:
            dfs(w)


for tc in range(1, 11):
    v, e = map(int, input().split())
    G = [[]*v for _ in range(v+1)]
    visited = [0] * (v+1)

    for i in range(e):
        u, v = map(int, input().split())
        G[u].append(v)

    S, G = map(int, input().split())
    dfs(S)

    if visited(G) == 1:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))

