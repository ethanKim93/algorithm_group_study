import sys
sys.stdin = open('input.txt')
# 3팀 코드

def dfs(s, V): # s 시작정점. V 마지막 정점(1번부터 시작하는 정점의 개수)
    stack = [] #빈 스택 생성
    visited = [0] * (V + 1) # 방문 여부를 검사할 행렬
    stack.append(s) # 시작점 스택에 넣음

    while stack:  # 스택이 빌때까지 반복문 돌려준다.
        now = stack.pop() # 지금 현재 스택을 꺼내어 현재 값에 할당
        visited[now] = 1 # 현재 들렀음을 표시(시작점)
        for i in range(1, V + 1):
            if visited[i] == 0 and ad[now][i]: # 방문하지 않았고 연결 되어 있다면 (값이 1이라면)
                stack.append(i)        # 스택에 더해줌

    if visited[V]: # 만약 끝점에 들른 흔적이 있다면?
        return 1   # 들렀다는 것을 확인
    else:
        return 0   # 안들렀다면 안들렀다는 것을 확인


T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split()) # 정점V와 간선E의 개수
    ad = [[0]*(V+1) for _ in range(V+1)]     # 노드를 인접행렬로 나타내기 위한 초기 값
    for i in range(E):
        n1, n2 = map(int, input().split())   #노드의 연결상태
        ad[n1][n2] = 1
    S, D = map(int, input().split())        #시작점과 끝점
    print('#{} {}'.format(tc, dfs(S, D)))