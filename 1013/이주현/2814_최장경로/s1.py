import sys
sys.stdin = open('sample_input.txt')

def DFS(idx, cnt):
    global result
    visited[idx] = True
    if cnt > result:
        result = cnt
    for i in graph[idx]:
        if not visited[i]:
            DFS(i, cnt+1)
            visited[i] = 0

T = int(input())

for tc in range(1, 1 + T):
    N, M = map(int,input().split())
    graph = [[] for i in range(N+1)]
    for i in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    result = 0

    for i in range(1, N+1):
        visited = [0] * (N+1)
        DFS(i, 1)
    print("#{} {}".format(tc, result))