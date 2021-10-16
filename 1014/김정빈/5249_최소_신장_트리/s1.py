# from pprint import pprint
# import sys
# sys.stdin = open("input.txt")
#5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리
def prim(V, start):
    minEdge[start] = 0 # 시작점 가중치는 0
    for _ in range(V):
        idx = 0 # 현재 정점 번호 초기화
        minV = 9999 # 최소 신장트리 비용
        for i in range(1, V+1):
            if not visited[i]: # 아직 정점이 신장트리에 포함되어있지 않고
                if minEdge[i] < minV: # 최소값이 적으면
                    idx = i # 정점 번호를 기억하고
                    minV = minEdge[i] #교체도 해줌
        visited[idx] = True # 다 골랐으면 방문여부 체크
        for w in range(V+1):
            if not visited[w] and adjMatrix[idx][w]: # 방문여부와 최소간선비용 최소보다 현재 w로 오는 간선이 있으면
                if minEdge[w] > adjMatrix[idx][w]: # 최소 간선비용보다 적으면
                    minEdge[w] = adjMatrix[idx][w] # 교체
    return sum(minEdge)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjMatrix = [[0]*(V+1) for _ in range(V+1)]
    visited = [False]*(V+1) # 방문여부
    minEdge = [9999]*(V+1) # 최소 가중치 초기화
    for _ in range(E):
        n1, n2, v = map(int, input().split())
        adjMatrix[n1][n2] = v # 가중치를 위치에 넣어줌
        adjMatrix[n2][n1] = v
    print('#{} {}'.format(tc, prim(V, 0)))