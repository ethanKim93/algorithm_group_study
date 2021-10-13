# -*- coding: utf-8 -*-

import copy
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))


# 백트래킹의 재귀를 종료시킬 변수, 현재 벽돌들의 상태를 나타내는 변수, 현재까지 깬 벽돌의 수가 변수로 필요하다.
# cnt는 구슬을 떨어트린 횟수를 나타내는 변수를 의미
# now_list는 현재 벽돌의 상태를 나타내는 변수를 의미
# pop_cnt는 현재까지 깬 벽돌의 수를 나타내는 변수를 의미
def backTracking(cnt, now_list, pop_cnt):
    global max_num

    # 만약 구슬을 N번 떨어트렸다면, 재귀를 종료한다.
    if cnt == N:
        # 현재까지 깬 벽돌의 수가 지금까지 확인한 상태 중 최대로 깬 벽돌의 수보다 크면
        # 이를 업데이트 한다.
        if max_num < pop_cnt:
            max_num = pop_cnt
        return

    # 구슬을 떨어트리는 도중에 다 깬 경우가 발생하면, 더 이상 볼 필요가 없으므로
    # 확인하지 않는다.
    if max_num == total_num:
        return

    # 구슬을 떨어트릴 위치를 for문을 통해 col 변수로 지정하고, 이 지점에 떨어트려본다.
    for col in range(W):
        # 구슬을 떨어트렸을 때 생기는 벽돌의 상태를 나타내는 temp_list와
        # 그 경우 깨게 되는 벽돌의 수를 temp_pop_cnt 변수에 저장한다.
        temp_list, temp_pop_cnt = getDrop(col, now_list)

        # 구슬을 떨어트렸으므로 cnt + 1와 현재 구슬을 떨어트린 상태와 이번 차례에 깬 벽돌의 수(temp_pop_cnt)를
        # pop_cnt에 더해주어 함수를 호출한다.
        backTracking(cnt + 1, temp_list, pop_cnt + temp_pop_cnt)
    return


# 벽돌을 떨어트렸을 때 변화는 상태와 깨게되는 벽돌의 수를 반환하는 함수
def getDrop(col, now_list):
    # 새로운 리스트로 형성하여 처리해준다.
    temp_list = copy.deepcopy(now_list)

    # 이번 차례에 깨트릴 벽돌의 수를 저장할 temp_pop_cnt 변수를 선언한다.
    temp_pop_cnt = 0

    # 처음으로 맞추게 될 변수 first_strike를 선언한다.
    # 이때 첫번째 인덱스에는 row의 값, 두번째 인덱스에는 col의 값, 세번째 인덱스에는 벽돌에 새겨진 숫자를 의미한다.
    first_strike = [0, col, 0]
    for r in range(H):
        if temp_list[r][col] > 0:
            first_strike[0] = r
            first_strike[2] = temp_list[r][col]
            temp_list[r][col] = 0
            temp_pop_cnt += 1
            break

    # 선형 큐를 선언하여, BFS를 통하여 현재 차례에서 깨지게 되는 모든 벽돌을 깨트린다.
    front = -1
    rear = 0
    queue = [[0, 0, 0]] * (W * H)
    queue[rear] = first_strike

    while front < rear:
        # 선형 큐에 대한 pop 연산으로,
        # temp_row, temp_col는 터진 벽돌의 row, col
        # bomb_numbers는 터진 벽돌에 새겨진 숫자를 의미한다.
        front += 1
        temp_row, temp_col, bomb_numbers = queue[front]

        # 벽돌에 새겨진 숫자 - 1 만큼의 범위를 터트리므로, 이 범위를 bomb_num을 통하여 순회한다.     
        for bomb_num in range(bomb_numbers):
            for direction in directions:
                # bomb_numbers = 4일 경우
                # bomb_num = 0, 1, 2, 3으로 순회하며 새로 터트릴 후보가 될 지역의 row와 col을 new_row, new_col에 저장한다.
                new_row = temp_row + direction[0] * bomb_num
                new_col = temp_col + direction[1] * bomb_num

                # 터트릴 후보의 벽돌의 변호가 1이면 추가적인 영향을 안끼치므로 깨트린 횟수만 증가시켜주고,
                # 번호가 1보다 크면, 선형 큐에 추가해주어 추가적인 폭발을 연산해준다.
                if 0 <= new_row < H and 0 <= new_col < W:
                    if temp_list[new_row][new_col] > 0:
                        if temp_list[new_row][new_col] == 1:
                            temp_list[new_row][new_col] = 0
                        else:
                            # 선형 큐의 push 연산
                            rear += 1
                            queue[rear] = [new_row, new_col, temp_list[new_row][new_col]]
                            temp_list[new_row][new_col] = 0
                        temp_pop_cnt += 1

    # 현재 경우에서 깨지게 되는 상황을 모두 확인한 후에 중력을 적용시켜준다.
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


# 전체 벽돌의 수를 세는 getTotal 함수
def getTotal(maps):
    cnt = 0
    for r in range(H):
        for c in range(W):
            # 벽돌이면, cnt를 하나 증가시킨다.
            if maps[r][c] > 0:
                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(H)]

    # 현재 테스트 케이스에 주어진 전체 벽돌의 수를 세어 total_num 변수에 저장한다
    total_num = getTotal(maps)
    # 가장 많이 벽돌을 깬 횟수를 저장 할 max_num 변수를 선언한다.
    max_num = 0
    # 백트래킹 시작
    backTracking(0, maps, 0)

    print("#{} {}".format(tc, total_num - max_num))
