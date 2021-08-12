import sys
sys.stdin = open("input.txt")

arrow = {"L": (0, -1), "R": (0, 1), "U": (-1, 0)}

for case in range(10):
    T = int(input())
    li = []

    for _ in range(100):
        li.append(list(map(int, input().split())))

    X = li[99].index(2)
    Y = 99
    X_adder = 0
    Y_adder = -1

    while Y > 0:
        if Y_adder == -1:
            if X + X_adder > 0 and li[Y][X - 1]:
                Y_adder, X_adder = arrow["L"]
            elif X + X_adder < 99 and li[Y][X + 1]:
                Y_adder, X_adder = arrow["R"]
        elif 0 <= X + X_adder <= 99 and li[Y][X + X_adder]:
            pass
        else:
            Y_adder, X_adder = arrow["U"]

        Y += Y_adder
        X += X_adder

    print("#{} {}".format(case + 1, X))