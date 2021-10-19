import sys
sys.stdin = open('input.txt')
from collections import deque


def BFS(sr, sc):
    cost = [[INF] * N for _ in range(N)]
    Q = deque()
    Q.append((sr, sc, 0))
    while Q:
        r, c, w = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if cost[nr][nc] > w + M[nr][nc]:
                    cost[nr][nc] = w + M[nr][nc]
                    Q.append((nr, nc, cost[nr][nc]))
    return cost


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, list(input()))) for _ in range(N)]
    INF = 1000000

    c = BFS(0, 0)
    print('#{} {}'.format(tc, c[N-1][N-1]))
