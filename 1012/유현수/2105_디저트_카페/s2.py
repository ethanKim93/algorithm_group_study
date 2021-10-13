import sys
sys.stdin = open('sample_input.txt')

dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def tour(r, c, direction, visited_cafe, cnt):
    global ans
    visited_cafe.append(cafe[r][c])
    print(r, c, direction, visited_cafe, cnt)
    if cnt == 3:
        nr = r + dirs[direction + 1][0]
        nc = c + dirs[direction + 1][1]
        if nr == first_r and nc == first_c:
            if ans < len(visited_cafe):
                ans = len(visited_cafe)
    for i in range(2):
        nr = r + dirs[direction + i][0]
        nc = c + dirs[direction + i][1]
        if 0 <= nr < N and 0 <= nc < N:
            if cafe[nr][nc] not in visited_cafe:
                if i:
                    tour(nr, nc, direction+i, visited_cafe, cnt+1)
                else:
                    tour(nr, nc, direction+i, visited_cafe, cnt)
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            first_r, first_c = i, j
            tour(i, j, 0, [], 1)
    print('#{} {}'.format(tc, ans))
