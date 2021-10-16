import sys
sys.stdin = open('sample_input.txt')


def DFS(r):
    for i in range(1, N+1):
        if not visited[i] and adj[r][i]:        # 아직 그룹에 속하지 않은, 지목한 조원
            visited[i] = 1                      # 조원 추가
            DFS(i)                              # 그 조원이 지목한 사람 탐색


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    base = list(map(int, input().split()))
    adj = [[0]*(N+1) for _ in range(N+1)]       # 인접 행렬
    visited = [0] * (N+1)                       # 그룹에 속했는지 여부 기록
    group = 0

    for i in range(M):
        r, c = base[i*2], base[i*2+1]
        adj[r][c] = adj[c][r] = 1               # 내가 너를 지목하든, 네가 나를 지목하든 같은 그룹

    for j in range(1, N+1):
        if not visited[j]:
            visited[j] = 1                      # 조원 등록
            DFS(j)                              # 깊이 우선 탐색
            group += 1                          # 그룹 수 1 증가
    print('#{} {}'.format(tc, group))