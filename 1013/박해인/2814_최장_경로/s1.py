import sys
sys.stdin = open('sample_input.txt')

def dfs(idx, cnt):
    global length

    if length < cnt:
        length = cnt

    for i in range(N+1):  # 인접 리스트 사용할 때와 diff
        if not visited[i] and adjM[idx][i]:  # not visited & 경로가 유효한가 체크 bixu.
            visited[i] = 1
            dfs(i, cnt+1)
            visited[i] = 0


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * (N+1)  # 1번부터 시작하는 간선 번호 -> 인덱스 번호 = 간선 번호 위해서 N+1로 설정
    adjM = [[0]*(N+1) for _ in range(N+1)]
    for i in range(M):
        s, e = map(int, input().split())
        adjM[s][e] = 1
        adjM[e][s] = 1

    length = 0  # 재귀 이용할 거니까 global로 선언
    for i in range(1, N+1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0

    print('#{} {}'.format(test_case, length))
