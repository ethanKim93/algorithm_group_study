import sys
sys.stdin = open('input.txt', 'r')


def prim(n):
    MST = [0] * N
    cost = [1000000000000] * N
    cost[n] = 0

    for _ in range(N - 1):
        # 최소 가중치 지점 찾기
        w = 0
        min_value = 10000000000000
        for k in range(N):
            if not MST[k]:
                if cost[k] < min_value:
                    w = k
                    min_value = cost[k]
        MST[w] = 1

        for l in range(N):
            # 노드간 최소 거리로 cost 갱신
            if not MST[l]:
                cost[l] = min(cost[l], dist[w][l])

    return sum(cost)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 섬의 개수
    X = list(map(int, input().split()))
    # 각 섬들의 정수인 X좌표
    Y = list(map(int, input().split()))
    # 각 섬들의 정수인 Y좌표
    E = float(input())
    # 해저터널 건설의 환경 부담 세율 실수 E

    dist = [[0] * N for _ in range(N)]
    # 각 섬마다 거리를 담은 배열
    for i in range(N):
        for j in range(N):
            dist[i][j] = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2
    # print(dist)

    answer = round(E*prim(0))

    print('#{} {}'.format(tc, answer))
