import sys
sys.stdin = open("input.txt")

row_adder = [0, 1, 0, -1]
col_adder = [1, 0, -1, 0]

T = int(input())

for case in range(T):
    N = int(input())

    li = [[0] * N for _ in range(N)]

    mode = 0
    row = 0
    col = 0
    for num in range(N**2):
        li[row][col] = num + 1
        if not (row + row_adder[mode] < N and col + col_adder[mode] < N and li[row + row_adder[mode]][col + col_adder[mode]] == 0):
            mode = (mode + 1) % 4
        row += row_adder[mode]
        col += col_adder[mode]

    print("#{}".format(case + 1))
    for i in range(N):
        print(*li[i])