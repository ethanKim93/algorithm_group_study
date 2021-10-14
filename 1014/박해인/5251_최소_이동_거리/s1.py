# MST 크루스칼? 다익스트라? 배열 이동이 아니니 크루스칼인듯??
# 다익스트라였다~~~~~~~~
import sys
sys.stdin = open('sample_input.txt')

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 상 하 좌 우

T = int(input())
for test_case in range(1, T+1):
    N, E = map(int, input().split())

    INF = float('inf')
    distance = [[INF]*(N+1) for _ in range(N+1)]
    for i in range(E):
        s, e, w = map(int, input().split())
        distance[s][e] = w

    v = [INF] * (N+1)
    v[0] = 0

    for i in range(N+1):
        for j in range(N+1):
            if v[i] + distance[i][j] < v[j]:
                v[j] = v[i]+distance[i][j]

    print('#{} {}'.format(test_case, v[N]))
