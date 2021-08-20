import sys
sys.stdin = open("sample_input.txt")

# DFS 정의 함수
def dfs(s, e, V):
    visited = [0]*(V+1)
    stack = []
    i = s               # 현재 방문한 정점 i
    visited[i] = 1      # 방문한 경우 0->1

    while i:            # 스택에 저장된 게 없으면 i=0
        for w in range(1, V+1):
            if adj[i][w] and visited[w] == 0:    # 인접한데 방문하지 않은 곳이 있으면
                stack.append(i)                  # 방문 경로 저장
                i = w                            # 새 방문지 이동
                visited[w] = 1                   # 방문한 노드로 저장

                if i == e:                       # 도착지를 찾는 경우
                    return 1
                break
        else:                   # 더이상 갈 곳이 없는 경우
            if stack:
                i = stack.pop() # 스택에 최근 갔던 곳으로 돌아가서 다시 찾기
            else:
                i = 0           # 스택에 저장된 게 없으면 루프 종료

    return 0                    # 경로중에 e 도착지를 못 찾는 경우

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    # 인접행렬 정의
    adj = [[0] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1         # 방향성 존재 n1 -> n2

    s, e = map(int, input().split())
    print('#{} {}'.format(tc, dfs(s, e, V)))
