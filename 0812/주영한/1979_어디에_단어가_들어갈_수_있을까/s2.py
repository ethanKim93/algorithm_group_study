import sys
sys.stdin = open("input.txt")

def check_word(grid, row, col, N, target):
    result = 0

    # row 방향으로 움직일 수 있는 리스트와 col 방향으로 움직일 수 있는 리스트를 directions로 둔다.
    directions = [[[1, 0], [-1, 0]], [[0, 1], [0, -1]]]

    # row 방향, col방향에 대해 확인한다.
    for each_direction in directions:
        # row방향, col방향에 대한 단어가 들어갈 수 있는 공간을 초기화한다.
        word_len = 0
        # + row 방향, - row 방향으로 확인해본다.
        for direction in each_direction:
            temp_row = row
            temp_col = col
            # 해당 영역이 배열 내부에 있고, 벽이 아니라면, 해당 영역을 확인한 것으로 보는 2로 두고,
            # 이동한다.
            while temp_row >= 0 and temp_row <= N-1 and temp_col >= 0 and temp_col <= N-1 and grid[temp_row][temp_col]:
                word_len += 1
                grid[temp_row][temp_col] = 2
                temp_row += direction[0]
                temp_col += direction[1]
        word_len -= 1
        if word_len == target:
            result += 1
    return result

T = int(input())

for tc in range(1, T + 1):
    cnt = 0
    N, K = map(int, input().split())

    # 주어진 입력에 대한 단어 퍼즐을 정의함
    grid = [0] * N
    for row in range(N):
        grid[row] = list(map(int, input().split()))

    for row in range(N):
        for col in range(N):
            # 이미 확인한 열, 행의 경우 확인하지 않는다.
            if grid[row][col] == 1:
                cnt += check_word(grid, row, col, N, K)

    print("#{} {}".format(tc, cnt))