import sys
sys.stdin = open("sample_input.txt")

T = int(input())

def bfs(s,g):
    q = []          # 큐 생성
    q.append(s)     # 시작점 인큐 #enQ
    visited[s] = 1  # 시작점 방문 표시
    while q:
        t = q.pop(0)    #deQ
        for w in adjList[t]:
            if visited[w] == 0:     # 인접 정점이 미방문이면
                if w == g:          # 인접 정점이 도착점이면
                    return visited[t]
                else:
                    q.append(w)         # 인접 정점 인큐
                    visited[w] = visited[t] + 1
    return 0                                    # 도착점을 못찾으면 0 리턴

for tc in range(1,T+1):
    V,E = map(int,input().split())
    edge = [input().split() for _ in range(E)]
    adjList = [[] for _ in range(V+1)]           # 인접리스트
    visited = [0] * (V+1)
    S,G = map(int,input().split())
    for i in range(E):
        n1 = int(edge[i][0])
        n2 = int(edge[i][1])
        adjList[n1].append(n2)
        adjList[n2].append(n1)
    print('#{} {}'.format(tc, bfs(S,G)))
