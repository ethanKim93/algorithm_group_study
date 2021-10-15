import sys
sys.stdin = open('sample_input.txt')


def prim(start, V):                     # prim 알고리즘 MST 가중치의 합을 리턴. (1~V번 노드)
    key = [INF] * (V + 1)               # key[i] : i가 MST에 연결되는 비용(가중치)
    key[start] = 0                      # 임의의 정점(시작지점) 초기화
    MST = [0] * (V+1)                   # 최소신장트리에 노드 사용 여부
    for _ in range(V):                  # 모든 정점이 MST에 포함될 때 까지
        u = 0
        minV = INF
        for i in range(V+1):
            if MST[i] == 0:
                if key[i] < minV:
                    u = i
                    minV = key[i]
        MST[u] = 1                      # key[u]가 최소인 u를 MST에 추가
        for v in range(V+1):
            if not MST[v] and adj[u][v]:
                if key[v] > adj[u][v]:  # u를 이용해 기존보다 더 작은 비용으로 MST에 연결된다.
                    key[v] = adj[u][v]
    return sum(key)


for tc in range(1, int(input())+1):
    INF = 10000
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]     # 인접 정점 리스트(가중치)
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w     # 무방향그래프에서 MST구성
        adj[n2][n1] = w

    print('#{} {}'.format(tc, prim(0,V)))
