import sys
sys.stdin = open('sample_input.txt')

def dfs(idx, cnt):
    global length

    visited[idx] = 1

    if cnt > length:
        length = cnt

    for i in adjL[idx]:
        if not visited[i]:
            dfs(i, cnt+1)
            visited[i] = 0

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    adjL = [[] for _ in range(N+1)]
    for i in range(M):
        s, e = map(int, input().split())
        adjL[s].append(e)
        adjL[e].append(s)

    length = 0
    for i in range(1, N+1):
        visited = [0] * (N+1)
        dfs(i, 1)

    print('#{} {}'.format(test_case, length))