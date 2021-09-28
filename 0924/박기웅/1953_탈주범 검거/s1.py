import sys
sys.stdin = open('sample_input.txt')

# 우하좌상
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
pipe = [
    [0 ,0 ,0, 0],           # 0이면 아무곳도 못감
    [1, 1, 1, 1],           # 상하좌우
    [0, 1, 0, 1],           # 상하
    [1, 0, 1, 0],           # 좌우
    [1, 0, 0, 1],           # 상우
    [1, 1, 0, 0],           # 하우
    [0, 1, 1, 0],           # 하좌
    [0, 0, 1, 1],           # 상좌
]


for tc in range(1, int(input())+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]

    # bfs 를 통해 시간 내에 갈 수 있는 곳 합산
    visited = [[0]*M for _ in range(N)]
    Q = [(R,C)]
    visited[R][C] = 1
    while Q:
        r, c = Q.pop(0)
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                # 현재 방향으로 터널이 뚤려 있고, 갈 위치의 터널 방향이 맞아야 갈 수 있음
                # 맨홀을 1로 두고 시작했으므로 현재 위치의 방문값이 L보다 작을 때까지 움직일 수 있음
                if pipe[tunnel[r][c]][i] and pipe[tunnel[nr][nc]][(i+2)%4] and visited[r][c] < L:
                    Q.append((nr, nc))
                    visited[nr][nc] = visited[r][c]+1
    ans = 0
    for i in visited:
        for j in i:
            if j:
                ans += 1
    print('#{} {}'.format(tc, ans))
