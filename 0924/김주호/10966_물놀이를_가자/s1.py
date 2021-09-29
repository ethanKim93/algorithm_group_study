from collections import deque

adder = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}


def BFS():
    while queue:
        row, col = queue.popleft()
        for arrow in range(4):
            y_adder, x_adder = adder[arrow]
            y = row + y_adder
            x = col + x_adder
            if 0 <= y < N and 0 <= x < M and distance[y][x] == -1:
                distance[y][x] = distance[row][col] + 1
                queue.append((y, x))


for case in range(int(input())):
    N, M = map(int, input().split())
    field = [input() for _ in range(N)]
    distance = [[-1] * M for _ in range(N)]
    queue = deque()

    for r in range(N):
        for c in range(M):
            if field[r][c] == 'W':
                queue.append((r, c))
                distance[r][c] = 0

    BFS()

    val = 0
    for r in distance:
            val += sum(r)

    print("#{} {}".format(case + 1, val))
