import sys
sys.stdin = open('sample_input.txt')

def bfs(v,s):
    q = [v]
    visited[v] = 1
    while q:
        t = q.pop(0)
        for j in range(V+1):
            if j in adj[t] and visited[j] == 0:
                q.append(j)
                visited[j] = visited[t] + 1
    if visited[s] - visited[v] > 0:
        return visited[s] - visited[v]
    else:
        return 0


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    # 인접 리스트
    adj = [[] for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    S, G = map(int, input().split())
    visited = [0] * (V+1)
    print('#{} {}'.format(tc, bfs(S, G)))
