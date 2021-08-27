



def BFS(S, G):
    Q = [] # 큐
    visted = [0] * (V + 1) #(트리 레벨이 나타남) 자식 노드로 내려 갈때 마다. 하나씩 증가
    Q.append(S) # 큐에 시작 노드를 집어 넣는다.
    visted[S] = 1 # 시작노드를 방문처리

    while Q:
        tmp = Q.pop(0) # 큐의 시작노드를 꺼내고
        if tmp == G: #종점노드와 같은 지 비교
            return visted[tmp] - 1 #시작노드를 1로 시작했으므로 -1을 해야 트리의 레벨이 나옴
        for i in range(V + 1): #행을 고정시키고 열을 기반으로 반복문을 돌며 인접 노드 탐색
            if adj[tmp][i] == 1 and visted[i] == 0: # 인접노드가 있고 방문하지 않은 노드이면
                Q.append(i) # 해당노드를 큐에 넣어준다.
                visted[i] = visted[tmp] + 1 # 방문처리
    return 0 # 못찾았을때 0 반환


import sys

sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # 노드수 #간선수
    Edge = [list(map(int, input().split())) for _ in range(E)]  # 엣지
    adj = [[0] * (V + 1) for _ in range(V + 1)] #인접행렬
    S, G = map(int, input().split())  # 출발노드와 도착노드
    for i, j in Edge:  # 인접행렬 초기화
        adj[i][j] = 1
        adj[j][i] = 1
    # print(S,G)
    print('#{} {}'.format(tc, BFS(S, G)))
