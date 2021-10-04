import sys
sys.stdin = open('sample_input.txt')

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def search(r, c, road, skill):
    global ans
    if road > ans:
        ans = road

    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0<= nc < N and not visited[nr][nc]:
            if moutain[r][c] > moutain[nr][nc]:
                search(nr,nc,road+1,skill)
            elif skill and moutain[r][c] > moutain[nr][nc] - K:
                tmp = moutain[nr][nc]
                moutain[nr][nc] = moutain[r][c]-1
                search(nr, nc, road +1, 0)
                moutain[nr][nc] = tmp
    visited[r][c] = 0

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    moutain = []
    for n in range(N):
        moutain.append(list(map(int, input().split())))

    max_height = 0
    for i in range(N):
        for j in range(N):
            if max_height < moutain[i][j]:
                max_height = moutain[i][j]

    visited = [[0]* N for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            if moutain[i][j] == max_height:
                search(i, j, 1, 1)

    print('#{} {}'.format(tc, ans))