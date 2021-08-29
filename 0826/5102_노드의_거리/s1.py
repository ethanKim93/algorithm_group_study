import sys
sys.stdin = open('sample_input.txt')

def bfs(V):
    q = [V]
    while q:# 큐 생성
        V = q.pop()      # dequeue 해서 t에 저장
        for w in range(1, V+1):
            if adjList[V][w] and not visited[w]:
                q.append(w)
                visited[w] = visited[V] + 1
                if w == end:
                    return visited[V]
    return 0


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split()) #V개의 노드, E개의 간선
    adjList = [[] for _ in range(V+1)] #인접 리스트
    visited = [0 for _ in range(V+1)] #방문여부
    for i in range(E):
        n1,n2 = map(int,input().split())
        adjList[n1].append(n2)
        adjList[n2].append(n1)
    start, end = map(int,input().split()) # 시작노드와 끝나는 노드
    #print(adjList)
    visited[start] = 1 #시작 노드 방문

    print('#{} {}'.format(tc, bfs([start])))
