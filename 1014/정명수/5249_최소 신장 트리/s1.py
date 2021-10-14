import sys
sys.stdin = open('input.txt')

def prim(start,V):
    MST[start] = 0          # 임의의 시작점 간선비용을 0으로 세팅
    cost = 0                # 최소신장트리비용
    for i in range(V+1):        # 1. 신장트리에 포함되지 않은 정점 중 최소 간선비용의 정점 찾기
        minV = INF
        minVertex = -1          # 최소 간선비용의 정점번호
        for j in range(V+1):
            if not visited[j] and minV>MST[j]:
                minV = MST[j]
                minVertex = j
        visited[minVertex] = 1
        cost += minV               # 간선비용 누적

        for j in range(V+1):        # 2. 선택된 정점 기준으로 신장트리에 연결되지 않은 타 정점과의 간선 비용 최소로 업데이트
            if not visited[j] and arr[minVertex][j] != 0 and MST[j] > arr[minVertex][j]:
                MST[j] = arr[minVertex][j]
    return cost

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    edge = [list(map(int,input().split())) for _ in range(E)]
    INF = 10000
    arr = [[0]*(V+1) for _ in range(V+1)]
    for case in edge:
        arr[case[0]][case[1]] = case[2]
        arr[case[1]][case[0]] = case[2]

    MST = [INF]*(V+1)
    visited = [0]*(V+1)
    print('#{} {}'.format(tc,prim(0,V)))