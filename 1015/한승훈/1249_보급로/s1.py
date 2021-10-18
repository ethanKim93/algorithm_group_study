import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maps = [list(map(int, input())) for _ in range(N)]
    dx = [0,0,-1,1]
    distance = [[10000] * N for _ in range(N)]
    distance[0][0] = 0
    queue = deque([(0, 0)])
    d = [0, 0, -1, 1]
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni, nj = i + d[k], j + d[k - 2]
            if 0 <= ni < N and 0 <= nj < N:
                plus = maps[ni][nj]
                if distance[ni][nj] > distance[i][j] + plus:
                    distance[ni][nj] = distance[i][j] + plus
                    queue.append((ni, nj))
    print('#{} {}'.format(tc, distance[N - 1][N - 1]))

