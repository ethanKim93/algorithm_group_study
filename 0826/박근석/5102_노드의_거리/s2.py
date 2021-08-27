import sys
sys.stdin = open('sample_input.txt')


def BFS(v):
    q = [v]
    visited[v] = 1
    while q:
        v = q.pop(0)
        for w in range(1, V+1):             # 인접한 노드 확인
            if adj[v][w] and not visited[w]:
                q.append(w)
                visited[w] = visited[v] + 1
                if w == G:
                    return visited[v]
    return 0

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    for i in range(E):
        x, y = map(int, input().split())
        adj[x][y] = adj[y][x] = 1
    S, G = map(int, input().split())

    print('#{} {}'.format(tc, BFS(S)))