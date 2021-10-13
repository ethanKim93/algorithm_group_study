import sys
sys.stdin = open('input.txt')


def prim(start, V):                             # MST 가중치의 합을 리턴하는 함수.
    key = [INF] * (V+1)                         # key[i] == i가 MST에 연결되는 비용
    key[start] = 0
    MST = [0] * (V+1)                           # MST에 포함 여부 표시
    for _ in range(V):                          # 모든 정점이 MST에 포함될 때 까지
        u = 0                                   # MST에 포함되지 않은 정점 중 key[u]가 최소인 u 찾기
        minV = INF
        for i in range(V+1):
            if MST[i] == 0:
                if key[i] < minV:
                    u = i
                    minV = key[i]
        MST[u] = 1                              # key[u]가 최소인 u를 MST에 추가
        for v in range(V+1):
            if MST[v] == 0 and adj[u][v] != 0:  # MST에 포함되지 않고 u에 인접인 v에 대해
                if key[v] > adj[u][v]:          # u를 이용해 기존보다 더 작은 비용으로 업데이트.
                    key[v] = adj[u][v]
    return sum(key)                             # MST 가중치의 합 리턴


V, E = map(int, input().split())
INF = 10000
adj = [[0] * (V+1) for _ in range(V+1)]         # 인접행렬

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u][v] = w
    adj[v][u] = w                               # 무방향 그래프에서 MST 구성

print(prim(1, V))