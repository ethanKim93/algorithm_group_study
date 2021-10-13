directions = ((1, 1), (1, -1), (-1, -1), (-1, 1))


def go(r, c, cnt, dir, temp_dessert_list):
    global max_cnt
    if cnt > 0 and r == target_r and c == target_c:
        if cnt > max_cnt:
            max_cnt = cnt
        return
    
    if dir > 3:
        return

    if cnt == 0:
        new_row = r + directions[dir][0]
        new_col = c + directions[dir][1]
        if 0 <= new_row < N and 0 <= new_col < N:
            if maps[new_row][new_col] not in temp_dessert_list:
                temp_dessert_list.append(maps[new_row][new_col])
                go(new_row, new_col, cnt + 1, dir, temp_dessert_list)
                temp_dessert_list.pop()
    else:
        for dir_change in range(2):
            new_row = r + directions[(dir + dir_change) % 4][0]
            new_col = c + directions[(dir + dir_change) % 4][1]
            if 0 <= new_row < N and 0 <= new_col < N:
                if maps[new_row][new_col] not in temp_dessert_list:
                    temp_dessert_list.append(maps[new_row][new_col])
                    go(new_row, new_col, cnt + 1, dir + dir_change, temp_dessert_list)
                    temp_dessert_list.pop()
    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    for r in range(N):
        for c in range(N):
            target_r = r
            target_c = c
            go(r, c, 0, 0, [])

    max_cnt = max_cnt if max_cnt > 0 else -1
    print("#{} {}".format(tc, max_cnt))