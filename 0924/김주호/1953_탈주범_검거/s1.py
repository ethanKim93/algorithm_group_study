op = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}
correct = {"U": "D", "R": "L", "D": "U", "L": "R"}
pipes = [
    [],
    ["U", "D", "L", "R"],
    ["U", "D"],
    ["L", "R"],
    ["U", "R"],
    ["R", "D"],
    ["L", "D"],
    ["L", "U"]
]

for case in range(int(input())):
    N, M, R, C, L = map(int, input().split())  # 세로 N, 가로 M, 맨홀 세로 위치 R, 가로 위치 C, 소요된 시간 L
    field = [list(map(int, input().split())) for _ in range(N)]
    check = [[0] * M for _ in range(N)]
    check[R][C] = 1
    queue = [(R, C, 1)]

    while queue:
        row, col, cnt = queue.pop(0)
        arrow = pipes[field[row][col]]

        for direction in arrow:
            y_adder, x_adder = op[direction]
            y = row + y_adder
            x = col + x_adder

            if 0 <= y < N and 0 <= x < M and field[y][x] != 0 and check[y][x] == 0 and \
                    correct[direction] in pipes[field[y][x]] and cnt < L:
                check[y][x] = 1
                queue.append((y, x, cnt + 1))

    total = 0
    for i in range(N):
        for j in range(M):
            total += check[i][j]

    print("#{} {}".format(case + 1, total))
