# 다익스트라 알고리즘 - 하나의 정점에서 다른 모든 정점으로 가는 최단 경로를 알려줌
# 풀이1 => 2에서 출발 다익스트라 알고리즘 + 다른 모든 정점에서 2로 출발하는 알고리즘??
# 풀이2 => 진출행렬을 진입행렬로 바꾸어서, 다익스트라 알고리즘으로 다른 모든 정점에서 2로 돌아오는 비용 계산
# 풀이2가 풀이1보다 좋아보여서 그걸로 했다.

import sys
sys.stdin = open('input.txt')

def dijkstra(x, direction):  # x: 출발 노드
    dist = [INF] * (N + 1)
    visited = [False] * (N + 1)

    dist[x] = 0
    cnt = 0
    # 최솟값 찾기
    while cnt != N-1:  # 이유??
        min_idx = 0
        min_value = INF
        for i in range(1, N+1):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]
        visited[min_idx] = True
        cnt += 1
        # 거리 갱신하기
        for i in range(1, N+1):
            if direction:  # in
                if not visited[i] and adjout[min_idx][i] + dist[min_idx] < dist[i]:
                    dist[i] = adjout[min_idx][i] + dist[min_idx]
            else:  # out
                if not visited[i] and adjin[min_idx][i] + dist[min_idx] < dist[i]:
                    dist[i] = adjin[min_idx][i] + dist[min_idx]
    return dist


T = int(input())

for tc in range(1, T+1):
    N, M, X = map(int, input().split())  # 집 1~N, M: 도로 수, X: 생일 집
    # 인접행렬
    INF = 987654321
    adjout = [[INF]*(N+1) for _ in range(N+1)]  # 진출. 일반
    adjin = [[INF]*(N+1) for _ in range(N+1)]  # 진입.
    for _ in range(M):
        x, y, c = map(int, input().split())
        adjout[x][y] = c
        adjin[y][x] = c
    # 다익스트라
    max_ans = 0
    distout = dijkstra(X, 0)
    distin = dijkstra(X, 1)
    # print(distin)
    # print(distout)

    for i in range(1, N+1):
        temp = distout[i] + distin[i]
        if temp > max_ans:
            max_ans = temp
    print('#{} {}'.format(tc, max_ans))




