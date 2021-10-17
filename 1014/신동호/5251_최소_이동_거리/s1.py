import sys
sys.stdin = open('sample_input.txt')

def Dijkstra(s, N):
    U = [0] * (N+1)
    U[s] = 1
    # 시작점 기준으로 D에 거리를 입력, 연결 안되어있다면 매우 큰 값 들어감
    for v in range(N+1):
        D[v] = A[s][v]
    
    # 아직 모든 정점이 연결되지 않았다면
    while sum(U) != N:
        min_w = 987654321
        for i in range(N+1):
            # 연결되지 않은 정점에 대해 다음에 연결할 최소 거리의 정점
            if min_w > D[i] and not U[i]:
                min_w = D[i]
                w = i
        # 연결 표시
        U[w] = 1 

        # 각각의 정점 v에 대해 기존의 거리, w를 거쳐서 가는 거리 중 더 작은 값을 넣어준다
        for v in range(N+1):
            D[v] = min(D[v], D[w]+A[w][v])


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    A = [[987654321] * (N+1) for _ in range(N+1)] # 각각의 정점에서 서로 연결하는 비용
    for _ in range(E):
        s, e, w = map(int, input().split())
        A[s][e] = w
    D = [0] * (N+1) # 각 정점에 연결하는데 드는 최소 비용들
    Dijkstra(0, N)
    print('#{} {}'.format(tc, D[N]))