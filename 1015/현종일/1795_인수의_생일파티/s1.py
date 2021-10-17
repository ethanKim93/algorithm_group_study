import sys
sys.stdin = open("input.txt")

# 아 진짜 모르겠다

def dijkstra(s, adj):
    adj[s] = 0

for tc in range(1, int(input())+1):
    N, M, X = map(int, input().split())

    adj1 = [[987654321] * (N+1) for _ in range(N+1)]
    adj2 = [[987654321] * (N+1) for _ in range(N+1)]

    for _ in range(M):
        x, y, c = map(int, input().split())
        adj1[x][y] = c
        adj2[y][x] = c

    dijkstra(X, adj1)
    dijkstra(X, adj2)

    max_value = 0

    print("#{} {}".format(tc, max_value))