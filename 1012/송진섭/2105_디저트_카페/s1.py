import sys
sys.stdin = open('sample_input.txt')

dr = [1, 1, -1, -1]                         # 하우, 상우, 하좌, 상좌
dc = [1, -1, 1, -1]


def dfs(row, col, road):
    global max_cnt
    if not len(road) % 4
    if max_cnt < len(road) - 2:
        max_cnt = len(road)
    else:
        visited[row][col] = 1
        for k in range(4):
            nr = row + dr[k]
            nc = col + dc[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                    if not cafe_map[nr][nc] in road:
                        dfs(nr, nc, road+[cafe_map[nr][nc]])
        visited[row][col] = 0
    if len(road) == 0:
        return -1


T = int(input())
for tc in range(1, 1+1):
    N = int(input())
    cafe_map = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    max_cnt = -1

    for i in range(N//2):
        for j in range(i+1, N//2):
            dfs(i, j, [cafe_map[i][j]])

