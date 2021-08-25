import sys
sys.stdin = open("sample_input.txt")


def backtracking(N, maze, start_pos, target):
    # 도착점에 도착할 경우 True를 반환
    if start_pos == target:
        return True

    # 각 방향에 대해 점검을 진행한다.
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    row = start_pos[0]
    col = start_pos[1]

    for direction in directions:
        # 방향으로 이동하여 미로 밖으로 벗어나는 인덱스나 벽에 부딪히는 경우에는
        # 무시하고, 적합한 경우에는 이동할 방향에 방문표시(벽표시)를 남기고 해당 방향으로
        # 재귀적으로 이동한다.
        row += direction[0]
        col += direction[1]
        if 0 <= row < N and 0 <= col < N and maze[row][col] != "1":
            maze[row][col] = "1"
            if backtracking(N, maze, [row, col], target):
                return True
            maze[row][col] = "0"
        row -= direction[0]
        col -= direction[1]
    return False



T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    maze = [list(input()) for _ in range(N)]

    # 시작점과 도착점에 대한 정보를 확인한다.
    for row in range(N):
        for col in range(N):
            if maze[row][col] == "2":
                start_pos = [row, col]
            if maze[row][col] == "3":
                target = [row, col]

    maze[start_pos[0]][start_pos[1]] = "1"
    print("#{} {}".format(tc, int(backtracking(N, maze, start_pos, target))))