import sys
sys.stdin = open("sample_input.txt")

adder = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

for case in range(int(input())):
    N = int(input())
    li = [list(map(int, input())) for _ in range(N)]

    Y = -2
    X = -2

    for row in range(N):
        if 2 in li[row]:
            Y = row
            break
    else:
        print("#{} {}".format(case + 1, 0))
        continue

    for col in range(N):
        if li[Y][col] == 2:
            X = col
            break

    stack = []
    flag = 0

    while True:
        for mode in range(4):
            Y_adder, X_adder = adder[mode]

            if not (0 <= Y + Y_adder < N and 0 <= X + X_adder < N):
                continue

            if li[Y + Y_adder][X + X_adder] == 3:
                flag = 1
                break
            elif li[Y + Y_adder][X + X_adder] == 0:
                stack.append((Y, X))
                Y += Y_adder
                X += X_adder
                li[Y][X] = 1
                break

        else:
            if stack:
                Y, X = stack.pop()
            else:
                break

        if flag:
            break

    print("#{} {}".format(case + 1, 1 if flag else 0))
