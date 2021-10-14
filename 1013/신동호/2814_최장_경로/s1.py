# import sys
# sys.stdin = open('sample_input.txt')

def DFS(v, cnt):
    global max_num, visited

    if not visited[v] == 1:
        visited[v] = 1
        for w in link[v]:
            if not visited[w]:
                DFS(w, cnt + 1)
        visited[v] = 0
    if cnt > max_num:
        max_num = cnt


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    link = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        link[a].append(b)
        link[b].append(a)
    s = [0] * (N+1)
    max_num = 0

    for i in range(1, N+1):
        visited = [0] * (N+1)
        DFS(i, 0)
    print('#{} {}'.format(tc, max_num+1))