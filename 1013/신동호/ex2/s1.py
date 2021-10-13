N = int(input())
E = list(map(int, input().split()))

visited = [0] * (N+1)

front = -1
rear = -1

def EnQueue(Q, x):
    global rear
    rear += 1
    Q[rear] = x

def deQueue(Q):
    global front
    front += 1
    return Q[front]

def BFS(V):
    global front, rear
    q = [0] * N
    EnQueue(q, V)
    visited[V] = 1
    while not front == rear:
        t = deQueue(q)
        print(t, end=' ')
        for u in link[t]:
            if not visited[u]:
                EnQueue(q, u)
                visited[u] = 1

link = [[] for _ in range(N+1)]
for i in range(0, len(E), 2):
    link[E[i]].append(E[i+1])
    link[E[i+1]].append(E[i])

BFS(1)