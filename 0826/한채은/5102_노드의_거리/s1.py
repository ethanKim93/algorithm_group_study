import sys
sys.stdin = open('sample_input.txt')

def BFS(v):
    q = [v]
    visited[v] = 1 # 지나간거 표시
    while q:
        v = q.pop(0)
        for w in range(1, V+1):     #인접 노드 확인
            if graph[v][w] and not visited[w]:
                q.append(w)
                visited[w] = visited[v]+1
                if W == G:
                    return visited[v]



    int(input())

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0] * (V+1) for _ in range(V+1)]   # 인덱스 번호 맞추기 위해서 V+1
    visited = [0] * (V+1)

    for i in range(E):
        x, y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1

    S, G = map(int, input().split())


    BFS(S)