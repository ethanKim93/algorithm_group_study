import sys
sys.stdin = open('sample_input.txt', 'r')
from collections import deque


def calc():
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    num = 987654321
    # 임의의 큰 값
    dist = [[num] * N for _ in range(N)]
    # 최단거리 배열
    dist[0][0] = 0
    # 시작값

    queue = deque()
    queue.append((0, 0))
    # 시작점을 queue 에 넣기
    while queue:
        row, col = queue.popleft()
        for i in range(4):
        # 사방탐색
            nr = row + dr[i]
            nc = col + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                price = 0
                # 높이 차
                if H[nr][nc] > H[row][col]:
                # 높이 차이가 있으면
                    price = H[nr][nc] - H[row][col]
                    # 높이 차이가 가중치
                if dist[nr][nc] > dist[row][col] + price + 1:
                # 새로 갈 좌표의 최단거리
                # => 현 위치의 최단거리 + 현 위치 - 새 위치의 가중치 + 1 (움직이는데 기본 비용)
                    dist[nr][nc] = dist[row][col] + price + 1
                    queue.append((nr, nc))
    return dist[N - 1][N - 1]
    # 도착점의 값 리턴


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(tc, calc()))


# 블로그에서 긁어온 설명

# 2차원 배열의 특정 위치에서 부터 인접 좌표들로 이동을 하면서 최소비용을 구하는 문제
# 가중치가 없다면 단순 bfs로 해결할 수 있음.
# 문제에서는 현재좌표의 높이와 새로운 좌표의 높이 차이가 있다면 ( 새로운 좌표가 높다면) 그 높이 만큼을 가중치로 계산함
# 시작점 (0,0)에서 BFS 탐색을 하면서 각 인접 좌표 (상하좌우)에 대해 간선완화를 진행
# 한 좌표의 상하좌우에 있는 새로운 좌표 계산
# 각 좌표가 범위내인지 확인
# 새로운 좌표의 높이가 현재의 높이보다 높다면 그 차이를 가중치로 계산
# 높이 차이가 없거나 새좌표가 더 낮으면 가중치는 1 (기본 비용)
# 새로운 좌표의 현재까지의 최소비용(시작점에서 부터의 최소비용)가 현 좌표를 찍고 가는 것 보다 높으면 새로운 비용으로 갱신
# 새좌표의 최소비용 > 현좌표 최소비용 + (현-새 높이차) 면 갱신
# 새 좌표를 큐에 넣기 : 그 좌표 부터 새 좌표를 찾기 위해서
# 반복이 끝나고 N-1,N-1에 있는 비용이 최소비용
