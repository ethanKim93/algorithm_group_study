import sys
sys.stdin = open('input.txt')
from pprint import pprint

def BFS(S, G):
    queue = []
    queue.append(S)
    visited[S] = 0      # 방문한 출발점에 지나온 간선 거리를 0으로 선언
    # / 평소처럼 1로 선언하면 간선을 거치지 않아도 1개의 간선을 건넌 것으로 표현
    while queue:
        t = queue.pop(0)
        for i in range(1, V+1):
            if adj[t][i] and visited[i] == -1:      # 간선이 있고, 방문하지 않았다면
                queue.append(i)                     # q에 방문할 정점을 쌓아주고
                visited[i] = visited[t] + 1         # 방문한 정점의 지나온 간선 수 = 지난 정점의 간선 수 +1
                if i == G:                          # 도착점에 방문하면
                    return visited[i]               # 지나온 간선 수를 반환
    return 0

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    line = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())    # 출, 도착점
    adj = [[0] * (V + 1) for _ in range(V + 1)]    # 인접행렬
    for i in range(E):
        n1, n2 = line[i][0], line[i][1]
        adj[n1][n2] = 1
        adj[n2][n1] = 1
    visited = [-1] * (V+1)    # 방문 결과를 저장할 리스트를 -1로 초기화(출발시 0으로 표기)
    print('#{} {}'.format(tc, BFS(S, G)))