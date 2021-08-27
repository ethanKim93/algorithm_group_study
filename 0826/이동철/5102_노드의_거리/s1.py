import sys
sys.stdin = open('sample_input.txt')


def bfs(S, G):
    queue = []
    visited = [0] * (V + 1)
    queue.append(S)
    visited[S] = 1
    while queue:
        t = queue.pop(0)
        for i in range(1, V + 1):
            # i는 1부터 노드의 개수까지
            if adj[t][i] == 1 and visited[i] == 0:
                # 인접행렬의 해당 행을 탐색 & 방문하지 않았으면
                queue.append(i)
                visited[i] = visited[t] + 1
                # visited에 최단거리 기록
                if i == G:
                    # i와 G가 같아지면, 즉 연결되면
                    return visited[i] - 1
    return 0
    #아니면 0으로 리턴


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    # V = 노드 개수, E = 방향성이 없는 간선 개수
    edge = [list(map(int, input().split())) for _ in range(E)]
    # E_list = 간선 정보
    S, G = map(int, input().split())

    adj = [[0]*(V + 1) for _ in range(V + 1)]
    # 인접행렬
    for i in edge:
        n1, n2 = i[0], i[1]
        adj[n1][n2] = 1
        adj[n2][n1] = 1

    print('#{} {}'.format(tc, bfs(S, G)))
