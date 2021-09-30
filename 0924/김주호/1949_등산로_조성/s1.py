adder = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}


def route(flag, now, r, c):
    global cnt, max_cnt
    cnt += 1
    for arrow in range(4):
        y_adder, x_adder = adder[arrow]
        y = r + y_adder
        x = c + x_adder
        if 0 <= y < N and 0 <= x < N:
            field[r][c] *= 100
            if now > field[y][x]:
                route(flag, field[y][x], y, x)
            elif flag and now > field[y][x] - K:
                route(False, now-1, y, x)
            field[r][c] //= 100

    if max_cnt < cnt:
        max_cnt = cnt
    cnt -= 1
    return


for case in range(int(input())):
    N, K = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]

    highest = 0
    highest_place = []
    for row in range(N):
        for col in range(N):
            if field[row][col] > highest:
                highest = field[row][col]
                highest_place.clear()
                highest_place.append((row, col))

            elif field[row][col] == highest:
                highest_place.append((row, col))

    cnt = 0
    max_cnt = 0
    for place in highest_place:
        route(True, field[place[0]][place[1]], *place)

    print("#{} {}".format(case + 1, max_cnt))

