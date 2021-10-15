import sys
sys.stdin = open('input.txt')

# 최소 신장트리로 하되, 모든 섬이 인접 할 수 있음
def prim(st):
    MST = [0]*N
    cost = [INF]*N
    cost[st] = 0
    
    for _ in range(N-1):
        # 최소 가중치 지점 찾기
        u = 0
        minV = INF
        for i in range(N):
            if not MST[i]:
                if cost[i] < minV:
                    u = i
                    minV = cost[i]

        MST[u] = 1

        # 노드간 최소 거리로 cost 갱신
        for v in range(N):
            if not MST[v]:
                cost[v] = min(cost[v], dist[u][v])

    return sum(cost)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    INF = 98765432100000
    # 각 섬간 거리를 나타내는 배열 정의
    dist = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = (X[i]-X[j])**2 + (Y[i]-Y[j])**2    
    
    print('#{} {}'.format(tc, round(E*prim(0))))