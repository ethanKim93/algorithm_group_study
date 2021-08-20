import sys
sys.stdin = open("sample_input.txt")


def dfs(s):
    visited[s] = 1
    stack.append(s)
    for w in range(1, V+1):
        if li[s][w] == 1 and not visited[w]:
            dfs(w)
    return stack


T = int(input())
for tc in range(1,T+1):
    stack = []
    V,E = map(int, input().split())
    li = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        u, v = map(int, input().split())
        li[u][v] = 1
    S, G = map(int,input().split())
    if G in dfs(S):
        result = 1
    else:
        result = 0
    print('#{} {}'.format(tc, result))
