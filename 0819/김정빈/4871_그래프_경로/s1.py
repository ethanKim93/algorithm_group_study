import sys
sys.stdin = open("input.txt")

def dfs(start, goal, V):
    stack = [] #경로
    visited = [0] * (V+1) #방문여부
    i = start #시작정점 방문으로 하고 시작
    visited[i] = 1 #방문여부 표시
    while i: #유효한 정점(1이있는곳)에 방문한 상태면
        for w in range(1, V+1): #인접, 방문안한 정점 w찾기
            if graph[i][w] == 1 and visited[w] == 0:
                stack.append(i) #현재 정점 경로에 저장
                i = w #방문
                visited[i] = 1
                if i == goal: #끝까지 들어간게 goal과 같으면
                    return 1
                break #아니면 처음부터
        else: #경로 없을떄
            if stack: #스택에 정점 있으면
                i = stack.pop() #하나 꺼내고 다시확인
            else: #정점없으면 더이상 길x
                i = 0
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s][e] = 1 #단방향, 갈수있는 곳 1로 표시
    start, goal = map(int, input().split())

    print('#{} {}'.format(tc, dfs(start,goal,V)))