import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for x in range(N):
        tmp_row = 0
        tmp_col = 0

        for y in range(N):

            if field[x][y]:
                tmp_row += 1
            if field[x][y] == 0 or y == N - 1:
                if tmp_row == K:
                    cnt += 1
                tmp_row = 0
            if field[y][x]:
                tmp_col += 1
            if field[y][x] == 0 or y == N - 1:
                if tmp_col == K:
                    cnt += 1
                tmp_col = 0

    print('#{} {}'.format(tc, cnt))

