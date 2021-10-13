import copy


def make_field(f, repeat=0, cnt=0):
    if repeat == N:
        global max_score

        if max_score < cnt:
            max_score = cnt
        return

    for col in range(W):
        field = copy.deepcopy(f)
        bomb = 0
        for row in range(H):
            if field[row][col] != 0:
                bomb = destroy(row, col, field[row][col], field)
                break

        for c in range(W):
            for r in range(H - 1, -1, -1):
                if field[r][c] == 0:
                    for step in range(r - 1, -1, -1):
                        if field[step][c] != 0:
                            field[r][c], field[step][c] = field[step][c], 0
                            break
                    else:
                        break

        make_field(field, repeat + 1, cnt + bomb)


def destroy(r, c, val, area):
    cnt = 1
    area[r][c] = 0
    for y in range(-(val-1), val):
        if 0 <= r + y < H and area[r + y][c] != 0:
            cnt += destroy(r + y, c, area[r + y][c], area)

    for x in range(-(val-1), val):
        if 0 <= c + x < W and area[r][c + x] != 0:
            cnt += destroy(r, c + x, area[r][c + x], area)

    return cnt


for case in range(int(input())):
    N, W, H = map(int, input().split())
    original = [list(map(int, input().split())) for _ in range(H)]

    block = 0
    for i in range(H):
        for j in range(W):
            if original[i][j] != 0:
                block += 1

    max_score = 0
    make_field(original)
    print("#{} {}".format(case + 1, block - max_score))
