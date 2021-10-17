import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, 1 + T):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    adj = [[0] * (N + 1) for _ in range(N + 1)]
    for edge in edges:
        adj[edge[0]][edge[1]] = adj[edge[1]][edge[0]] = edge[2]

    visited = [False] * (N + 1)
    weights = [999] * (N + 1)
    weights[0] = 0

    for i in range(N + 1):
        for j in range(N + 1):
            if adj[i][j] != 0 and weights[j] > adj[i][j] + weights[i]:
                weights[j] = adj[i][j] + weights[i]

    print("#{} {}".format(tc, weights[-1]))

