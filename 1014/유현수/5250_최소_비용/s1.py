import sys
sys.stdin = open('sample_input.txt')
from collections import deque


def BFS(sr, sc):
    cost = [[INF] * (N) for _ in range(N)]
    cost[sr][sc] = 0
    queue = deque()
    queue.append((sr, sc))
    while queue:
        r, c = queue.popleft()
        # for i in range(N):
        #     print(cost[i])
        # print()
        # print(r, c)
        for i in range(4):
            nr = r + dirs[i][0]
            nc = c + dirs[i][1]
            if 0 <= nr < N and 0 <= nc < N:
                # 인접한 위치의 높이가 더 높을 때
                if matrix[nr][nc] > matrix[r][c]:
                    # 최소 비용 업데이트
                    if cost[nr][nc] > (matrix[nr][nc] - matrix[r][c]) + 1 + cost[r][c]:
                        cost[nr][nc] = matrix[nr][nc] - matrix[r][c] + 1 + cost[r][c]
                        queue.append((nr, nc))
                # 인접한 위치 높이가 같거나 낮을 떼
                else:
                    # 최소 비용 업데이트
                    if cost[nr][nc] > cost[r][c] + 1:
                        cost[nr][nc] = cost[r][c] + 1
                        queue.append((nr, nc))
    return cost[N-1][N-1]


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    INF = 10000000

    print('#{} {}'.format(tc, BFS(0, 0)))
