import sys
sys.stdin = open("sample_input.txt")

def BFS(maze, start_row, start_col, end_row, end_col):
    # 미로의 총 길이를 함수 내에서 재정의
    N = len(maze)
    
    # 시작점에 대한 값을 check_queue에 넣고 맵에서 출발점과 도착점에 대한
    # 값을 수정한다. (0 일때 움직일 수 있게 하기위해서)
    check_queue = [[start_row, start_col]]
    maze[start_row][start_col] = 1
    maze[end_row][end_col] = 0

    # 각 4개 방향에 대하여 정의한다.
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    # 큐가 공백이 될 때 까지 반복한다.
    while check_queue:
        # dequeue한 값을 temp_pos로 두고 이때 행/열을 temp_row, temp_col로 둔다.
        temp_pos = check_queue.pop(0)
        temp_row = temp_pos[0]
        temp_col = temp_pos[1]
        
        # 만약 dequeue한 값이 도착점일 경우, 거리를 반환한다.
        if temp_row == end_row and temp_col == end_col:
            return maze[temp_row][temp_col] - 2

        # 각 방향에 대해 이동할 수 있는 행/열 값을
        # new_row, new_col로 두고, 해당 값이 미로 내에 있고, 이동할 수 있는
        # 조건에 들어가면 해당 위치를 check_queue에 추가해준다.
        # 또한 미로에서 해당 지역을, dequeue한 값으로 부터 1을 더한 값으로 업데이트한다.
        # (깊이를 확인하기 위한 작업)
        for direction in directions:
            new_row = temp_row + direction[0]
            new_col = temp_col + direction[1]
            if 0 <= new_row < N and 0 <= new_col < N and not maze[new_row][new_col]:
                check_queue.append([new_row, new_col])
                maze[new_row][new_col] = maze[temp_row][temp_col] + 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    
    # 출발 점의 행/열 값과 도착 점의 행/열 값을 확인
    for row in range(N):
        for col in range(N):
            if maze[row][col] == 2:
                start_row, start_col = row, col
            if maze[row][col] == 3:
                end_row, end_col = row, col

    print("#{} {}".format(tc, BFS(maze, start_row, start_col, end_row, end_col)))