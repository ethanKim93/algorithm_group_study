V, E = map(int, input().split())
edge = list(map(int, input().split()))

adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    adjL[n1].append(n2)

print(adjL)

def bfs(s, V):
    q = [0] * V
    front = -1
    rear = -1
    visited = [0]*(V+1)
    rear += 1               # 시작점 인큐
    q[rear] = s
    visited[s] = 1         # 시작점 visited
    while front != rear:      #큐가 비어있지 않으면
        front += 1            #디큐해서 t에 저장
        t = q[front]
        print(t)
        for i in adjL[t]:        # t에 인접하고 미방문인 모든 i에 대해
            if  visited[i] == 0:
                rear += 1              # 인큐 i
                q[rear] = i
                visited[i] = visited[t] + 1     # i 방문표시

bfs(1, V)