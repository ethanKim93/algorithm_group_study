import copy
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

def backTracking(cnt, now_list, pop_cnt):
    global max_num
    if cnt == N:
        if max_num < pop_cnt:
            max_num = pop_cnt
        return

    if max_num == total_num:
        return

    for col in range(W):
        temp_list, temp_pop_cnt = getDrop(col, now_list)
        backTracking(cnt + 1, temp_list, pop_cnt + temp_pop_cnt)
    return
    
def getDrop(col, now_list):
    temp_list = copy.deepcopy(now_list)
    temp_pop_cnt = 0
    # get first strike point information (row, col, number)
    first_strike = [0, col, 0]
    for r in range(H):
        if temp_list[r][col] > 0:
            first_strike[0] = r
            first_strike[2] = temp_list[r][col]
            temp_list[r][col] = 0
            temp_pop_cnt += 1
            break

    # set linear queue
    front = -1
    rear = 0
    queue = [[0, 0, 0]] * (W * H)
    queue[rear] = first_strike

    while front < rear:
        front += 1
        temp_row, temp_col, bomb_numbers = queue[front]
        for bomb_num in range(bomb_numbers):
            for direction in directions:
                new_row = temp_row + direction[0] * bomb_num
                new_col = temp_col + direction[1] * bomb_num
                if 0 <= new_row < H and 0 <= new_col < W:
                    if temp_list[new_row][new_col] > 0:
                        if temp_list[new_row][new_col] == 1:
                            temp_list[new_row][new_col] = 0
                        else:
                            rear += 1
                            queue[rear] = [new_row, new_col, temp_list[new_row][new_col]]
                            temp_list[new_row][new_col] = 0
                        temp_pop_cnt += 1
    applyGravity(temp_list)
    return temp_list, temp_pop_cnt

def applyGravity(temp_list):
    for c in range(W):
        start_row = 0
        for r in range(H):
            if temp_list[r][c] == 0:
                for row_idx in range(r - 1, start_row - 1, -1):
                    temp_list[row_idx + 1][c] = temp_list[row_idx][c]
                    temp_list[row_idx][c] = 0
                start_row += 1
    return 

def getTotal(maps):
    cnt = 0
    for r in range(H):
        for c in range(W):
            if maps[r][c] > 0:
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(H)]
    total_num = getTotal(maps)
    max_num = 0
    backTracking(0, maps, 0)
    print("#{} {}".format(tc, total_num - max_num)) 