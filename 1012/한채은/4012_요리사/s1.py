import sys
sys.stdin = open('sample_input.txt')

def dfs(idx, total):
    global res
    # 재료 개수만큼 돌면서
    if idx == N // 2:
        a, b = 0, 0
        for i in range(N):
            for j in range(N):
                # 방문 했으면 a에 저장
                if visited[i] and visited[j]:
                    a += S[i][j]
                # 방문 안했으면 b에 저장
                elif not visited[i] and not visited[j]:
                    b += S[i][j]
        res = min(res, abs(a-b))

    # 중복 탐색 방지
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = 1
            dfs(idx+1, total + 1)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    res = 99999
    dfs(0, 0)
    print(res)
