import sys

sys.stdin = open('sample_input.txt')


def DFS(idx, cnt):
    global max_count
    if cnt > max_count:         # 최장 거리 갱신
        max_count = cnt

    for v in adj[idx]:          # 인접 노드중 하나 골라서
        if not visited[v]:      # 방문 안한 노드일 때
            visited[idx] = 1    # 방문체크
            DFS(v, cnt + 1)     # 다음 노드로 이동
            visited[idx] = 0    # 방문체크 초기화


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]              # 인접노드그래프
    visited = [0] * (N + 1)                     # 방문여부
    max_count = -1                              # 최대거리

    for _ in range(M):
        x, y = map(int, input().split())        # 무방향그래프이므로 두 노드 모두 간선을 연결
        adj[x].append(y)
        adj[y].append(x)

    for i in range(1, N+1):                     # 1부터 N 까지의 노드를 전부 DFS
        DFS(i, 1)
    print('#{} {}'.format(tc, max_count))