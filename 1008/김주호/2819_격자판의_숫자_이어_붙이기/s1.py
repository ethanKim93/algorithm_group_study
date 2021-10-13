from collections import deque
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for case in range(int(input())):
    field = [list(map(int, input().split())) for _ in  range(4)]
    queue = deque()

    for r in range(4):
        for c in range(4):
            queue.append((r, c, 1, field[r][c]))
    nums = set()
    while queue:
        row, col, step, num = queue.popleft()
        for to in range(4):
            y = row + dy[to]
            x = col + dx[to]
            if 0 <= y < 4 and 0 <= x < 4:
                if step < 6:
                    queue.append((y, x, step + 1, num * 10 + field[y][x]))
                else:
                    nums.add(num * 10 + field[y][x])

    print("#{} {}".format(case + 1, len(nums)))
