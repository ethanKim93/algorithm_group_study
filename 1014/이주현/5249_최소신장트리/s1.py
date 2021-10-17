import sys
sys.stdin = open('sample_input.txt')

def prim(start, V):  # 시작지점, 노드수
    key = [inf] * (V+1)  # 가중치 넣을 리스트
    visited = [0] * (V+1)  # 방문 여부 확인 리스트
    key[start] = 0  # 초기값 0으로 지정
    for _ in range(V):
        u = 0
        minV = inf
        for i in range(V+1):
            if not visited[i] and key[i] < minV:
                u = i
                minV = key[i]
        visited[u] = 1
        for v in range(V+1):
            if not visited[v] and adj[u][v]:
                if key[v] > adj[u][v]:
                    key[v] = adj[u][v]
    return sum(key)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]
    inf = 10000
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = adj[n2][n1] = w  # 방향 x
    print('#{} {}'.format(tc, prim(0, V)))