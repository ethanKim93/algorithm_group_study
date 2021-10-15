import sys
sys.stdin = open('sample_input.txt')


def BFS():
    q = [[0, 0]]
    while q:
        r,c = q.pop(0)
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                diff = 0                                    # 높이 차이 초기화
                if region[nr][nc] > region[r][c]:           # 지도상 높이가 높은 경우 높이 차이를 갱신
                    diff = region[nr][nc]-region[r][c]
                if cost[nr][nc] > cost[r][c] + diff + 1:    # 이동할 위치의 기존 비용보다 현재의 비용이 적으면
                    cost[nr][nc] = cost[r][c] + diff + 1    # 기존 비용을 갱신
                    q.append([nr, nc])                      # 큐에 추가
    return cost[N-1][N-1]                                   # 큐가 소진되면 비용 배열의 우측하단 값 반환


T = int(input())
dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]

for tc in range(1, T+1):
    N = int(input())
    region = [list(map(int, input().split())) for _ in range(N)]
    cost = [[N * 1000] * N for _ in range(N)]               # 비용 배열 초기화
    cost[0][0] = 0
    print('#{} {}'.format(tc, BFS()))