import sys
sys.stdin = open("input.txt")

def dfs(start, goal, V):
    stack = [] #경로
    visited = [0] * (V+1)                      #방문여부
    i = start                                  #시작정점 방문으로 하고 시작
    visited[i] = 1                               #방문여부 표시
    while i:     #i가 0이 아닐떄                    #유효한 정점(1이있는곳)에 방문한 상태면
        for w in range(1, V+1):                        #인접, 방문안한 정점 w찾기
            if graph[i][w] == 1 and visited[w] == 0:
                stack.append(i)                         #현재 정점 경로에 저장
                i = w                                   #방문
                visited[i] = 1
                if i == goal:                           #끝까지 들어간게 goal과 같으면
                    return 1
                break                                   #아니면 처음부터
        else:                                           #경로 없을떄
            if stack:#스택이 비면 false 하나라도 있으면 True #스택에 정점 있으면
                i = stack.pop()                         #하나 꺼내고 다시확인
            else:                                       #정점없으면 더이상 길x
                i = 0
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)] #이유: 교수님이 2차원에서 하는걸 설명 for문 안쓰면 앝은복사...
    for _ in range(E):                      #얕은복사가 됭서 1번 인덱스에 3을 넣으면 모든 인덱스에 3들감
        s, e = map(int, input().split())
        graph[s][e] = 1 #단방향, 갈수있는 곳 1로 표시
    start, goal = map(int, input().split())

    # print('#{} {}'.format(tc, dfs(start,goal,V)))
    print(graph)


    def dfs(s, V):  # s 시작정점, V 마지막 정점(1번부터 시작하는 정점의 개수)
        stack = []  # 지나온 정점을 저장(경로)
        visited = [0] * (V + 1)  # 정점의 방문여부를 표시
        # 시작정점은 무조건 방문 (별도로 처리) 이후에는 가능한 정점만 방문
        i = s  # 시작정점을 방문 (방문중인 정점의 번호 i)
        visited[i] = 1  # i 정점에 방문했음을 표시
        print(node[i])  # 방문 정점의 이름 표시(정점에서 할 일)
        while i:  # 유효한 정점은 0 < i, 정점에 방문한 생태면
            for w in range(1, V + 1):  # 인접하고 방문안한 정점 w 찾기기
                if adj[i][w] == 1 and visited[w] == 0:
                    stack.append(i)  # 현재 정점을 경로로 저장
                    i = w  # w에 방문 (현재 방문한 정점을 i)
                    visited[i] = 1
                    print(node[i])
                    break  # 다른 w 찾기 중단(for문 탈출)
            else:  # 다음 방문할 정점이 없는 경우
                # 지나온 경로중 가장 가까운 정점을 꺼내 i로 지정
                if stack:  # 스택이 비어있지 않은경우
                    i = stack.pop()
                else:  # 경로가 남아있지 않으므로 종료
                    i = 0  # 없는 정점을 방문정점 번호로 설정..
        return  # def dfs(s, V):


    #          A  B  C  D  E  F  G
    adj = [[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 1, 0, 0, 0, 0],  # A
           [0, 1, 0, 0, 1, 1, 0, 0],  # B
           [0, 1, 0, 0, 0, 1, 0, 0],  # C
           [0, 0, 1, 0, 0, 0, 1, 0],  # D
           [0, 0, 1, 1, 0, 0, 1, 0],  # E
           [0, 0, 0, 0, 1, 1, 0, 1],  # F
           [0, 0, 0, 0, 0, 0, 1, 0]]  # G
    node = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

    '''
    7 8
    1 2
    1 3
    ...
    '''
    # V, E = map(int, input().split())
    # ad = [[0]*(V+1) for _ in range(V+1)]
    # for _ in range(E):
    #     n1, n2 = map(int, input().split())
    #     ad[n1][n2] = 1
    #     ad[n2][n1] = 1
    dfs(1, 7)