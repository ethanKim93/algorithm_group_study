row_adder = [0, 1, 0, -1]
col_adder = [1, 0, -1, 0]

T = int(input())

for case in range(T):
    N = int(input())

    li = [[0] * N  for _ in range(N)]

    num = 1
    mode = 0
    row = col = 0
    while num <= N ** 2:
        if row < N and col < N and li[row + row_adder[mode]][col + col_adder[mode]] != 0:
            li[row][col] = num
            row += row_adder[mode]
            col += col_adder[mode]
