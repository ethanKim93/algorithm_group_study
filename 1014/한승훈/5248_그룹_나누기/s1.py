import sys
sys.stdin = open('sample_input.txt')
import time

start = time.time()
def dfs(start):
    for k in range(1, N+1):
        if group[start][k] and not visited[k]:
            visited[k] = 1
            dfs(k)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    groups = list(map(int, input().split()))
    group = [[0]*(N+1) for _ in range(N+1)]
    visited = [0] * (N+1)
    cnt = 0
    for i in range(M):
        group[groups[2*i]][groups[2*i+1]] = group[groups[2*i+1]][groups[2*i]] = 1
    for j in range(1, N+1):
        if not visited[j]:
            visited[j] = 1
            dfs(j)
            cnt += 1
    print('#{} {}'.format(tc, cnt))
print("time :", time.time() - start)


