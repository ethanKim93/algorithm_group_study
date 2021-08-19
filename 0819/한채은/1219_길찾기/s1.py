import sys
sys.stdin = open("input.txt")

def dfs(v):
    visited[v] = 1

    for w in range(1, V + 1):
        if G[v][w] == 1 and not visited[w]:
            dfs(w)


for _ in range(10):

    V = 100
    tc, E = map(int, input().split())
    tmp = list(map(int, input().split()))
    G = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)

    for i in range(E):
        s, e = tmp[2*i], tmp[2*i+1]
        G[s][e] = 1

    dfs(0)

    if visited[99] == 1:
        print("#{}".format(tc), 1)
    else:
        print("#{}".format(tc), 0)