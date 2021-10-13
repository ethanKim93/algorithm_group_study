from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for case in range(int(input())):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    check = [[True] * N for _ in range(N)]

    queue = deque()
    min_num = N
    max_step = 0
    flag = False

    for row in range(N):
        for col in range(N):
            if check[row][col]:
                step = 0
                start_num = N * N
                queue.append((row, col))
                while queue:
                    r, c = queue.popleft()
                    start_num = min(start_num, field[r][c])
                    step += 1
                    check[r][c] = False
                    for to in range(4):
                        y = r + dy[to]
                        x = c + dx[to]
                        if 0 <= y < N and 0 <= x < N and check[y][x]:
                            if field[r][c] + 1 == field[y][x] or field[r][c] - 1 == field[y][x]:
                                queue.append((y, x))

                if step >= max_step:
                    if step == max_step:
                        min_num = min(min_num, start_num)
                    else:
                        min_num = start_num

                    max_step = step

    print("#{} {} {}".format(case + 1, min_num, max_step))
