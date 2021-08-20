import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) #V:노드 E:간선 6, 5
    graph = [[0]*V for _ in range(V)]
    for _ in range(E):
        s, e = map(int, input().split()) #출발도착간선노드
        graph[s-1][e-1] = 1
    S, G = map(int, input().split()) #존재확인할 출/도착

    stack = [S-1] #경로에 기본 출발지정
    visited = [0]*V #방문표시할 리스트
    visited[S-1] = 1 #첫번째 방문표시
    ans = 0
    while stack: #스택 안비면
        for w in range(V): #012
            if graph[stack[-1]][w] == 1 and visited[w] == 0: #순회하며 간선이 있고 방문하지 않았던게 있으면
                stack.append(w) #스택쌓고, 방문기록
                visited[w] = 1

                if stack[-1] == G-1: #어딘가 끝까지 들어갔을 때 그게 도착노드면
                    ans = 1 #정답이고 for? while? 탈출
                break
        else:
            #만약 스택 안비었는데 정점도착이 아니면(탈출안하니까)
            stack.pop() #마지막 하나 빼고 while 다시돌게(간선찾으러)

        if ans: #1이면
            break
    print('#{} {}'.format(tc,ans))