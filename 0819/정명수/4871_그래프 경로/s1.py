import sys
sys.stdin = open("input.txt")

T = int(input())
def dfs(v):
    visited[v] = 1
    for i in range(len(arr[v])):
        if visited[i] == 0 and arr[v][i] == 1:
            dfs(i)

for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a][b] = 1
    S, G = map(int, input().split())
    dfs(S)
    if visited[G] == 1:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))

