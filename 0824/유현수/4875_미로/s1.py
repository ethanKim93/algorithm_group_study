import sys
sys.stdin = open('sample_input.txt')


def dfs(r, c):
    global ans
    if r == er and c == ec:
        ans = 1
        return
    else:
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if maze[nr][nc] != 1 and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    dfs(nr, nc)
                    visited[nr][nc] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]

    # 출발지(2), 목적지(3) 인덱스 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sr, sc = i, j
            elif maze[i][j] == 3:
                er, ec = i, j

    # 미로찾기
    visited = [[0] * N for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    ans = 0
    dfs(sr, sc)
    print('#{} {}'.format(tc, ans))