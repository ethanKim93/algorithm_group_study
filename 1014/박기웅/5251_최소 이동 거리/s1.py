import sys
sys.stdin = open('sample_input.txt')

def dijkstra(start):
    key[start] = 0

    for _ in range(N):              # 시작점 제외 모든 정점 순회
        u = 0
        minV = INF
        for i in range(N+1):        # MST에 포함되지 않은 정점 중 가중치 최소 정점 u 선택
            if not MST[i]:
                if key[i] < minV:
                    u = i
                    minV = key[i]
        MST[u] = 1                  

        for v in range(N+1):        # 인접한 정점 중 해당 정점의 가중치보다 현재 정점에서 가중치를 더한 값이 작은 경우 갱신
            if not MST[v] and adj[u][v]:
                key[v] = min(key[v], key[u]+adj[u][v])

    return key[N]                   # 도착점의 가중치 반환
                
    
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    INF = 1000000
    adj = [[0]*(N+1) for _ in range(N+1)]
    key = [INF]*(N+1)
    MST = [0]*(N+1)
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w
    print('#{} {}'.format(tc, dijkstra(0)))

    

