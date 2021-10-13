import sys
sys.stdin = open("sample_input.txt")

def dfs(idx, cnt):
    global max_len
    visited[idx] = True
    if cnt > max_len:
        max_len = cnt
    for i in field[idx]:
        if not visited[i]:
            dfs(i, cnt+1)
            visited[i] = 0

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    field = [[] for i in range(n+1)]
    max_len = 0
    for i in range(m):
        x, y = map(int, input().split())
        field[x].append(y)
        field[y].append(x)

    for i in range(1,n+1):
        visited = [0] * (n+1)
        dfs(i, 1)

    print('#{} {}'.format(tc, max_len))