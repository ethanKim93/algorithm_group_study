import sys
sys.stdin = open("sample_input.txt")

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def work(r, c, road, skill):
    global ans
    if road > ans: ans = road

    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:

            if mountain[r][c] > mountain[nr][nc]:
                work(nr, nc, road + 1, skill)

            elif skill and mountain[r][c] > mountain[nr][nc] - K:
                tmp = mountain[nr][nc]  # 기록
                mountain[nr][nc] = mountain[r][c] - 1
                work(nr, nc, road + 1, 0)  # 스킬 사용
                mountain[nr][nc] = tmp  # 원상복구

    visited[r][c] = 0

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())

    mountain = [list(map(int,input().split())) for _ in range(N)]
    max_h = 0

    for i in range(N):
        for j in range(N):
            if max_h < mountain[i][j]:
                max_h = mountain[i][j]

    visited = [[0] * N for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_h:
                work(i, j, 1, 1)  # 좌표, 길, 스킬

    print("#{} {}".format(tc, ans))

