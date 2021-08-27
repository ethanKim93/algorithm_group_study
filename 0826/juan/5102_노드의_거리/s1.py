import sys
sys.stdin = open('sample_input.txt')

def BFS(v):
    q = [v]                                     # queue 에 출발 노드 enqueue
    visited[v] = 1                              # 현재 간선을 지나지 않았지만(지나간 간선 의 수 = 0 이지만) 1로 시작해서 마지막에 조정해줄 예정
    while q:                                    # queue 가 채워져있는 동안 반복
        v = q.pop(0)                            # dequeue
        for w in range(1, V+1):                 # 1~V번 노드까지 현재 노드와 인접한 노드 탐색
            if adj[v][w] and not visited[w]:    # 인접해 있으면서 방문하지 않은 노드는
                q.append(w)                     # queue에 추가하고
                visited[w] = visited[v] + 1     # 이전 노드의 간선 수보다 1 증가
                if w == G:                      # 만약 지금 인접한 노드의 번호가 도착지점이라면
                    return visited[v]           # 도착지까지 오면서 지나온 간선의 수는 visited에 저장된 직전 노드가 지나간 간선의 수와 같으므로 visited[v]를 반환
    return 0                                    # 출발 노드에 인접한 모든 노드를 다 순회하고도 도착지에 도달하지 못하면 0 반환

T = int(input())
for tc in range(1, T+1):
    V,E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]     # 인접 행렬 초기화
    visited = [0] * (V+1)                       # 방문 여부 및 지나간 간선의 수 초기화
    for i in range(E):                          # 인접 행렬 정보 입력
        x,y = map(int, input().split())
        adj[x][y] = adj[y][x] = 1
    S,G = map(int, input().split())

    print('#{} {}'.format(tc, BFS(S)))