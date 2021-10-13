import sys
sys.stdin = open('sample_input.txt')

def dfs(start, cnt):
    global max_cnt
    visited[start] = 1

    if cnt > max_cnt:
        max_cnt = cnt
    for j in range(1, N+1):
        if maps[start][j] and not visited[j]:
            dfs(j, cnt + 1)
    visited[start] = 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    maps = [[0] * (N+1) for _ in range(N+1)]
    visited = [0] * (N+1)
    lines = [list(map(int, input().split())) for _ in range(M)]
    max_cnt = 0
    for line in lines:
        maps[line[0]][line[1]] = maps[line[1]][line[0]] = 1
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i,1)
    print('#{} {}'.format(tc, max_cnt))
