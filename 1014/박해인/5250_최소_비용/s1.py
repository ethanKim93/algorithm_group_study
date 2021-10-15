# SWEA 1249 문제 풀어보기
import sys
sys.stdin = open('sample_input.txt')

from collections import deque
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 상 하 좌 우

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]
    INF = float('inf')  # 양의 무한대
    distance = [[INF] * N for _ in range(N)]
    # distance 배열에 최소 비용 누적.
    distance[0][0] = 0
    queue = deque()
    queue.append((0, 0))

    while queue:
        y, x = queue.popleft()
        for dy, dx in move:
            my, mx = dy+y, dx+x
            if 0 <= my < N and 0 <= mx < N:
                cost = 1
                if H[my][mx] > H[y][x]:
                    cost += H[my][mx] - H[y][x]
                if distance[my][mx] > distance[y][x]+cost:
                    distance[my][mx] = distance[y][x]+cost
                    queue.append((my, mx))

    print('#{} {}'.format(test_case, distance[-1][-1]))