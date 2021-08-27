import sys
sys.stdin = open("sample_input.txt")

def bfs(S, G):
    front = rear = -1
    q = [0]*(V+1)            # 큐 생성
    visited = [0] * (V + 1)  # 방문록 초기화
    rear += 1                # enqueue
    q[rear] = S
    visited[rear] = 1        # 방문 도장찍음

    while front != rear:     # q가 비어있지 않으면
        front += 1           # dequeue
        t = q[front]         # dequeue 해서 t 에 저장

        if t == G:           # 도착지인지 확인
            return visited[t]

        for w in adjList[t]:    # t와 인접한 정점 w 중에서
            if not visited[w]:
                rear += 1       # w를 enqueue
                q[rear] = w
                visited[w] = visited[t] + 1  # 루트 노드로부터의 거리로 방문록 갱신
    return 0

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    adjList = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2 = map(int,input().split())
        adjList[n1].append(n2)
        adjList[n2].append(n1)
    S, G = map(int, input().split())
    print('#{} {}'.format(tc, bfs(S,G)))