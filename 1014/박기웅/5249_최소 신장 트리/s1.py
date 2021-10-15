import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def prim(V, start):
    key[start] = 0                          # 시작점의 가중치 초기화
    MST = [0]*(V+1)                         # 최소 신장 트리 초기화 
    for _ in range(V):                      # 모든 정점 순회
        u = 0
        minV = INF
        for i in range(1, V+1):             # key값이 가장 작은 정점 u 가져오기
            if not MST[i]:                  # 최소 신장트리에 선택되지 않은 정점 중에서
                if key[i] < minV:           # 최소 비용인 정점과 그 때의 가중치를 저장
                    u = i                   
                    minV = key[i]
        
        MST[u] = 1                          # MST에 해당 정점 u 포함
        for v in range(V+1):
            if not MST[v] and adj[u][v]:    # MST에 선택되지 않은 정점 중 u와 인접한 정점 중에서
                if key[v] > adj[u][v]:      # 인접한 정점과의 가중치가 현재 정점의 가중치보다 작으면 갱신
                    key[v] = adj[u][v]
    return sum(key)
        
           
for tc in range(1, T+1):
    V, E = map(int, input().split())
    INF = 2000000
    key = [INF]*(V+1)                       # 정점 V 와 연결된 가중치 초기화
    adj = [[0]*(V+1) for _ in range(V+1)]   # 간선 간 연결 확인 및 가중치 저장 배열

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w
        adj[n2][n1] = w

    # 0번 노드에서 시작
    print('#{} {}'.format(tc, prim(V, 0)))
