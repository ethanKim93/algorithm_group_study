import sys
sys.stdin = open('sample_input.txt')


def DFS(start, length):
    global max_length
    visited[start] = 1
    if length > max_length:
        max_length = length
    for i in adj[start]:
        if not visited[i]:
            DFS(i, length+1)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]

    for _ in range(M):
        n1, n2 = map(int, input().split())
        adj[n1].append(n2)
        adj[n2].append(n1)
    max_length = 0

    for i in range(1,N+1):
        visited = [0] * (N+1)
        DFS(i, 1)
    print('#{} {} '.format(tc, max_length))