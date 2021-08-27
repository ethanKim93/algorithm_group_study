import sys
sys.stdin = open("sample_input.txt")

adder = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

for case in range(int(input())):
    N = int(input())

    maze = [list(map(int, list(input()))) for _ in range(N)]

    Y = 0
    X = 0

    for r in range(N):
        if 2 in maze[r]:
            Y = r
            break
    else:
        print("#{} {}".format(case + 1, 0))
        continue

    for c in range(N):
        if 2 == maze[Y][c]:
            X = c
            break

    queue = [(Y, X)]
    maze[Y][X] = -1
    front = -1
    rear = 0

    result = 0

    while front != rear:
        front += 1
        Y, X = queue[front]
        for delta in range(4):
            Y_arrow, X_arrow = Y + adder[delta][0], X + adder[delta][1]
            if 0 <= Y_arrow < N and 0 <= X_arrow < N:
                if maze[Y_arrow][X_arrow] == 3:
                    result = -maze[Y][X] - 1
                    front = rear
                    break
                elif not maze[Y_arrow][X_arrow]:
                    maze[Y_arrow][X_arrow] = maze[Y][X] - 1
                    queue.append((Y_arrow, X_arrow))
                    rear += 1

    print("#{} {}".format(case + 1, result))
