import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(row, col):
    cost = [[987654321] * N for _ in range(N)]
    # 각 노드의 최소비용을 담을 배열
    cost[row][col] = 0
    # 시작 좌표 0으로 초기화
    queue = deque()
    queue.append((row, col))
    while queue:
        r, c = queue.popleft()
        # 현재 좌표
        for i in range(4):
            # 상,하,좌,우 탐색
            nr = r + dr[i]
            nc = c + dc[i]
            # 새로운 행,열 좌표
            if 0 <= nr < N and 0 <= nc < N:
                if cost[nr][nc] > cost[r][c] + maps[nr][nc]:
                    # 이동 후 지역의 최소비용이
                    # 이동 전의 최소비용과 이동 후 지역의 복구비용의 합보다 클 경우 갱신
                    cost[nr][nc] = cost[r][c] + maps[nr][nc]
                    queue.append((nr, nc))

    return cost[N - 1][N - 1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maps = [list(map(int, input())) for _ in range(N)]
    # 0, 0 에서 출발해서 N-1, N-1 에서 도착

    print('#{} {}'.format(tc, bfs(0, 0)))
