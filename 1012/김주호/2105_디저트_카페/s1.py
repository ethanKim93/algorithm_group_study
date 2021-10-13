dy = [1, 1, -1, -1]
dx = [1, -1, -1, 1]
R = [1, 0, -1, 0]
L = [0, 1, 0, -1]


def square(row, col, mode=0, step=1, right=1, left=0):
    if mode > 1 and right == 0 and left == 1:
        global max_step
        if max_step < step + 1:
            max_step = step + 1
        return

    if mode < 2:
        start = mode
        end = start + 2
    else:
        if max_step // 2 > step:
            return
        if right > 0:
            start = 2
        else:
            start = 3
        end = start + 1

    for to in range(start, end):
        y = row + dy[to]
        x = col + dx[to]
        if 0 <= y < N and 0 <= x < N and check[field[y][x]]:
            check[field[y][x]] = False
            square(y, x, to, step + 1, right + R[to], left + L[to])
            check[field[y][x]] = True


for case in range(int(input())):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    check = [True] * 101

    max_step = 0
    for i in range(N - 2):
        for j in range(1, N - 1):
            if field[i][j] != field[i + 1][j + 1]:
                check[field[i][j]] = False
                check[field[i + 1][j + 1]] = False
                square(i + 1, j + 1)
                check[field[i][j]] = True
                check[field[i + 1][j + 1]] = True

    print("#{} {}".format(case + 1, max_step if max_step != 0 else -1))
