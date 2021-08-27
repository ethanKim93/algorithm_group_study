import sys
sys.stdin = open('input.txt')

move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for tc in range(1, 11):
    N = input()
    maze = [list(map(int, input())) for _ in range(16)]
    start_col = 0
    start_row = 0
    answer = 0

    for i in maze:
        if 2 in i:
            start_col = i.index(2)
            break
        start_row += 1

    bfs_queue = [(start_row, start_col)]
    while bfs_queue:
        check = bfs_queue.pop(0)
        for row, col in move:
            next_row = check[0] + row
            next_col = check[1] + col

            if next_row == -1 or next_row == 16 or next_col == -1 or next_col == 16:
                continue

            if maze[next_row][next_col] == 0:
                bfs_queue.append((next_row, next_col))
            elif maze[next_row][next_col] == 3:
                answer = 1
                break

        maze[check[0]][check[1]] = 1
        if answer:
            break

    print('#{} {}'.format(tc, answer))