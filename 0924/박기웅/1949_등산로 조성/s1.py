import sys
sys.stdin = open('sample_input.txt')

# 우, 하, 좌, 상
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
# i, j 는 좌표, l은 지나온 경로의 길이, K 는 깎을 수 있는 길이, h는 현재 위치의 높이
def dfs(i, j, l, K, h):
    global maxl
    if maxl < l:
        maxl = l
    visited[i][j] = 1

    for w in range(4):
        ni, nj = i+di[w], j+dj[w]
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            if h > maps[ni][nj]:
                dfs(ni, nj, l+1, K, maps[ni][nj])
            else:
                # 갈 길이 없으면 가능한 공사일 경우 공사 진행
                if h > maps[ni][nj]-K:
                    # K를 더 이상 쓰지 못하도록 0으로 갱신
                    # K = 0 을 해버리면 이 이하에 모든 경로에서 K=0으로 되버림
                    # 현재 위치보다 하나 작게 만들어야 최대로 길게 갈 수 있음
                    dfs(ni, nj, l+1, 0, h-1)

    # 지나온 길 초기화
    visited[i][j] = 0

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]

    # 최고점 먼저 찾기
    maxh = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] > maxh:
                maxh = maps[i][j]
    maxl = 0
    # 방문기록 2d list
    visited = [[0] * N for _ in range(N)]
    # 시작점의 좌표를 찾아 dfs를 통해 찾아 나서기
    for i in range(N):
        for j in range(N):
            if maps[i][j] == maxh:
                dfs(i, j, 1, K, maxh)

    print('#{} {}'.format(tc, maxl))


