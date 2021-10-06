dy = [0, 1]
dx = [1, 0]


def load(score, row=0, col=0):
    global minimum
    if score > minimum:
        return

    if row == N-1 and col == N-1:
        if score < minimum:
            minimum = score
        return

    for i in range(2):
        y = row + dy[i]
        x = col + dx[i]
        if 0 <= y < N and 0 <= x < N:
            load(score + field[y][x], y, x)


for case in range(int(input())):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    minimum = 10 * N * N

    load(field[0][0])
    print("#{} {}".format(case + 1, minimum))
