directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
def bfs(row, col):
    global start_pos, max_value, visited

    if visited[row][col] == 1:
        return
    
    front = -1
    rear = 0
    queue = [0] * (N * N)
    queue[rear] = [row, col]
    visited[row][col] = 1

    temp_pos = maps[row][col]
    temp_value = 1

    while (front < rear):
        front += 1
        temp_row, temp_col = queue[front]
        for direction in directions:
            new_row = temp_row + direction[0]
            new_col = temp_col + direction[1]
            if 0 <= new_row < N and 0 <= new_col < N:
                if abs(maps[new_row][new_col] - maps[temp_row][temp_col]) == 1 and not visited[new_row][new_col]:
                    if temp_pos > maps[new_row][new_col]:
                        temp_pos = maps[new_row][new_col]
                    temp_value += 1
                    visited[new_row][new_col] = 1
                    rear += 1
                    queue[rear] = [new_row, new_col]

    if max_value == temp_value:
        if temp_pos < start_pos:
            start_pos = temp_pos
    if max_value < temp_value:
        start_pos = temp_pos
        max_value = temp_value
    return

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for __ in range(N)]
    start_pos = 0
    max_value = 0

    for row in range(N):
        for col in range(N):
            bfs(row, col)
    
    print("#{} {} {}".format(tc, start_pos, max_value))