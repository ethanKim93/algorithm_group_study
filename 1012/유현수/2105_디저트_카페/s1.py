import sys
sys.stdin = open('sample_input.txt')

dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def tour(r, c, cnt, direction, stack, desserts):
    global ans
    print(r, c, cnt, direction, stack, desserts)
    stack.append(cafe[r][c])
    print(stack)
    if cnt == 3:
        for i in range(4):
            nr = r + dirs[i][0]
            nc = c + dirs[i][1]
            if nr == first_r and nc == first_c and ans < desserts:
                ans = desserts
    elif not cnt:
        for i in range(4):
            nr = r + dirs[i][0]
            nc = c + dirs[i][1]
            if 0 <= nr < N and 0 <= nc < N:
                if cafe[nr][nc] not in stack:
                    tour(nr, nc, cnt+1, i, stack, desserts+1)
    else:
        for i in range(2):
            nr = r + dirs[direction+i][0]
            nc = c + dirs[direction+i][1]
            if 0 <= nr < N and 0 <= nc < N:
                if cafe[nr][nc] not in stack:
                    if i:
                        tour(nr, nc, cnt+1, direction+i, stack, desserts+1)
                    else:
                        tour(nr, nc, cnt, direction, stack, desserts+1)
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            first_r, first_c = i, j
            tour(i, j, 0, 0, [], 1)
            print(ans)
    print('#{} {}'.format(tc, ans))
