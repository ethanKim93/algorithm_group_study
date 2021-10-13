import sys
sys.stdin = open('sample_input.txt')

def dfs(idx, ans):
    global answer
    visited[idx] = 0 # 방문 표시
    ans += 1 # 이동 횟수 증가
    if answer < ans: # 최댓값 갱신
        answer = ans
    for i in graph[idx]: # 이동가능한 노드 확인
        if visited[i]:
            dfs(i, ans)
    visited[idx] = 1 # 방문 초기화


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    visited = [1 for _ in range(N+1)] # 방문을 표시할 배열
    temp = [list(map(int,input().split())) for _ in range(M)]
    graph = [[] for _ in range(N+1)]
    answer = 0

    for a, b in temp:
        graph[a].append(b)
        graph[b].append(a)

    for i in range(N):
        dfs(i,0)

    print('#{} {}'.format(t, answer))