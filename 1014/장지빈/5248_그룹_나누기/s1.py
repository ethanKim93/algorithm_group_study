import sys
sys.stdin = open('input.txt')
from pprint import pprint

def find(V):
    for i in range(1, N+1):
        if not visited[i] and adj[V][i]:
            visited[i] = 1
            find(i)
    return
for tc in range(1, int(input())+1):
    ans = 0
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    adj = [[0]*(N+1) for _ in range(N+1)]
    visited = [0] * (N+1)
    for i in range(M):
        a, b = li[i*2], li[(i*2)+1]
        adj[a][b] = 1
        adj[b][a] = 1
    # pprint(adj)
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            find(i)
            ans += 1
    print('#{} {}'.format(tc, ans))