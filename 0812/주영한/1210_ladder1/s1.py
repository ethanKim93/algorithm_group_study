import sys
sys.stdin = open("input.txt")


def block_check(grid, row, col):
    if row < 0 or row > 99 or col < 0 or col > 99 or grid[row][col] == 0:
        return True
    return False


def climing(grid, start_row, start_col):
    # 우회전, 좌회전, 올라가는 방향을 나타내는 directions 을 정의
    side_directions = [[0, 1], [0, -1]]
    direction = 0
    while True:
        if start_row == 0:
            return start_col
        # 양쪽 체크
        side_block = True
        for side_direction in side_directions:
            temp_row = start_row + side_direction[0]
            temp_col = start_col + side_direction[1]
            if block_check(grid, temp_row, temp_col):
                # 사이드 방향이 막혀있으면 여기서 돌아감
                continue
            # 사이드 방향이 안막혔을 경우 여기서 False 반환
            side_block = False
            direction = side_direction

        # 양쪽 다 막혔으면 위로 이동하고 While 문 처음부터 다시 시작
        if side_block:
            start_row -= 1
            continue

        # 뚫린 쪽으로 막힐때 까지 이동
        while True:
            temp_row = start_row + direction[0]
            temp_col = start_col + direction[1]
            if block_check(grid, temp_row, temp_col):
                start_row -= 1
                break
            start_row = temp_row
            start_col = temp_col


T = 10
for tc in range(1, T+1):
    dummy = input()
    ladder_grid = [0] * 100
    start_row, start_col = 0, 0
    for row in range(100):
        ladder_grid[row] = list(map(int, input().split()))
    for col in range(100):
        if ladder_grid[-1][col] == 2:
            start_row, start_col = 99, col
    end_col = climing(ladder_grid, start_row, start_col)

    print("#{} {}".format(tc, end_col))
