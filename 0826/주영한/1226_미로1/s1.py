import sys
sys.stdin = open("input.txt")


def BFS(maze, start_row, start_col, end_row, end_col):
    check_queue = [[start_row, start_col]]
    maze[start_row][start_col] = 1
    maze[end_row][end_col] = 0

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while check_queue :
        temp_pos = check_queue.pop(0)
        temp_row = temp_pos[0]
        temp_col = temp_pos[1]

        if temp_row == end_row and temp_col == end_col:
            return 1

        for direction in directions:
            new_row = temp_row + direction[0]
            new_col = temp_col + direction[1]
            if not maze[new_row][new_col]:
                check_queue.append([new_row, new_col])
                maze[new_row][new_col] = maze[temp_row][temp_col] + 1
    return 0

for tc in range(1, 11):
    num = input()
    maze = [list(map(int, list(input()))) for _ in range(16)]
    for row in range(100):
        for col in range(100):
            if maze[row][col] == 2:
                start_row, start_col = row, col
            if maze[row][col] == 3:
                end_row, end_col = row, col

    print("#{} {}".format(tc, BFS(maze, start_row, start_col, end_row, end_col)))