import sys
sys.stdin = open("input.txt")


def DFS(maze, start_row, start_col, end_row, end_col):
    cnt = 0
    check_stack = [[start_row, start_col]]
    maze[start_row][start_col] = 1
    maze[end_row][end_col] = 0

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while check_stack :
        cnt += 1
        temp_pos = check_stack.pop()
        temp_row = temp_pos[0]
        temp_col = temp_pos[1]

        if temp_row == end_row and temp_col == end_col:
            return [1, cnt]

        for direction in directions:
            new_row = temp_row + direction[0]
            new_col = temp_col + direction[1]
            if not maze[new_row][new_col]:
                check_stack.append([new_row, new_col])
                maze[new_row][new_col] = 1
    return [0]


for tc in range(1, 11):
    num = input()
    maze = [list(map(int, list(input()))) for _ in range(100)]
    for row in range(100):
        for col in range(100):
            if maze[row][col] == 2:
                start_row, start_col = row, col
            if maze[row][col] == 3:
                end_row, end_col = row, col

    print("#{} {}".format(tc, " ".join(map(str, DFS(maze, start_row, start_col, end_row, end_col)))))