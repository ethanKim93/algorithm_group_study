import sys
sys.stdin = open('sample_input.txt')


def dfs(start, end, V):
    visted = [0] * (V+1)
    visted[start] = 1
    i = start
    stack = [start]
    while i != 0:
        for w in range(1, V+1):
            if adj[i][w] == 1 and visted[w] == 0:
                visted[w] = 1
                stack.append(i)
                i = w
                break
        else:
            if stack:
                i = stack.pop()
            else:
                i = 0
    if visted[end] == 1:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]

    for i in range(E):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1
    start, end = map(int, input().split())
    ans = dfs(start, end, V)
    print('#{} {}'.format(tc, ans))
