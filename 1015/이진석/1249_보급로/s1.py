import sys
from collections import deque
sys.stdin = open('input.txt')

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for tc in range(1, int(input())+1):
    N = int(input())
    INF = 10*(N**2)
    maps = [list(map(int, list(input()))) for _ in range(N)]    # 출발 : 0,0 도착 : N-1, N-1
    cost = [[INF] * N for _ in range(N)]                        # 각 노드의 최소비용을 담을 배열

    q = deque()
    cost[0][0] = 0
    q.append((0,0))         # 시작좌표 enQ
    while q:
        r, c = q.popleft()  # 현재 좌표 deQ
        for d in delta:     # 상,하,좌,우 탐색
            nr = r + d[0]   # 새로운 행,열 좌표
            nc = c + d[1]
            if 0 <= nr < N and 0 <= nc < N:                     # 인덱스가 유효할 때
                # 이동 후 지역의 최소비용이 이동 전의 최소비용과 이동 후 지역의 복구비용의 합보다 작을경우 갱신
                if cost[nr][nc] > cost[r][c] + maps[nr][nc]:
                    cost[nr][nc] = cost[r][c] + maps[nr][nc]
                    q.append((nr,nc))                           # 이동 후 좌표 enQ

    print('#{} {}'.format(tc, cost[N-1][N-1]))