import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def bfs(start, end):
    visit = [0]*(V+1)
    visit[start] = 1
    queue = [start]
    while queue:
        a = queue.pop(0)
        for i in range(1, V+1):
            if adj[a][i] and not visit[i]:
                queue.append(i)
                visit[i] = visit[a] + 1
                if i == end:
                    return visit[a]
    return 0

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        x, y = map(int, input().split())
        adj[x][y] = adj[y][x] = 1
    start, end = map(int, input().split())

    print('#{} {}'.format(tc, bfs(start, end)))


