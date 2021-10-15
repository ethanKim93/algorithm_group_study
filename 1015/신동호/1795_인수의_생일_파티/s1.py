import sys
sys.stdin = open('input.txt')
# 다익스트라 X에서 출발하는 경우와 X로 도착하는 경우로 행렬 둘 나눠서 계산

def Dijkstra(s, adjL):
    D = [987654321] * (N+1)
    visited = [False] * (N+1)
    D[s] = 0

    for _ in range(N):
        min_v = 987654321
        min_idx = -1
        for i in range(1, N+1):
            if not visited[i] and D[i] < min_v:
                min_v = D[i]
                min_idx = i
        
        visited[min_idx] = True

        for i in range(1, N+1):
            if D[i] > adjL[min_idx][i] + D[min_idx]:
                D[i] = D[min_idx] + adjL[min_idx][i]

    return D
    

T = int(input())

for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    adjL = [[987654321] * (N+1) for _ in range(N+1)]
    adjL_back = [[987654321] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        adjL[x][y] = c
        adjL_back[y][x] = c
    # 각 점에서 X로 도착, X에서 각 점으로 도착
    D1 = Dijkstra(X, adjL)
    D2 = Dijkstra(X, adjL_back)

    max_dist = -1
    for i in range(1, N+1):
        # 모든 지점에서 X 경유 왕복 시간
        if max_dist < D1[i] + D2[i]: 
            max_dist = D1[i] + D2[i]
    print('#{} {}'.format(tc, max_dist))