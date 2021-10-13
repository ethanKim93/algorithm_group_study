import sys
sys.stdin = open('sample_input.txt', 'r')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# 탐색을 마치고 돌아왔을 때 이미 벽돌이 지워진 게임판을 사용할 수는 없기 때문에
# 깊은 복사로 게임판을 복사하는 함수 deepcopy()를 만든다.
# def deepcopy(lst):
#     new_lst = []
#     for y in range(len(lst)):
#         temp = []
#         for x in range(len(lst[y])):
#             temp.append(lst[y][x])
#         new_lst.append(temp)
#     return new_lst


# 떨어뜨린 구슬이 벽돌을 부수고 연쇄작용으로 부숴지는 탐색은 BFS를 진행하였다.
def erase_bricks(y, x, cur_bricks):
    Q = [(y, x, cur_bricks[y][x])]
    cur_bricks[y][x] = 0

    erased_bricks = 1
    while Q:
        cur_y, cur_x, cur_power = Q.pop(0)

        for p in range(1, cur_power):
            for d in range(4):
                new_y, new_x = cur_y + p * dy[d], cur_x + p * dx[d]
                if -1 < new_y < H and -1 < new_x < W and cur_bricks[new_y][new_x] != 0:
                    if cur_bricks[new_y][new_x] != 1:
                        Q.append((new_y, new_x, cur_bricks[new_y][new_x]))
                    erased_bricks += 1
                    cur_bricks[new_y][new_x] = 0

    return erased_bricks


# 기존에는 y축 방향으로 쭉 벽돌을 훑으면서 벽돌을 모은 다음에 다시 차곡차곡 쌓는 방식
# def sort_bricks(cur_bricks):
#     for x in range(W):
#         cur_w_bricks = []
#         for y in range(H - 1, -1, -1):
#             if cur_bricks[y][x] != 0:
#                 cur_w_bricks.append(cur_bricks[y][x])
#                 cur_bricks[y][x] = 0
#
#         for h in range(len(cur_w_bricks)):
#             cur_bricks[H - 1 - h][x] = cur_w_bricks[h]


# 새로운 방식은 y축 방향으로 처음부터 훑으면서 벽돌을 만날때마다 벽돌을 쌓아야할 위치를 바꿔주는 방식
def sort_bricks(cur_bricks):
    for x in range(W):
        prev = H - 1
        for y in range(H - 1, -1, -1):
            if cur_bricks[y][x]:
                if prev != y:
                    cur_bricks[prev][x], cur_bricks[y][x] = cur_bricks[y][x], cur_bricks[prev][x]
                prev -= 1


# 구슬을 떨어뜨린 횟수 차와 위치에 대한 탐색은 dfs 로 진행하고
# dfs() 함수 안에 벽돌을 지우는 함수 erase_bricks()와
# 지워진 벽돌을 정돈하는 함수 sort_bricks()를 따로 만들어 분리하였다.
def dfs(result, k, bricks):
    global max_result
    if k == N:
        if max_result < result:
            max_result = result
        return

    for w in range(W):
        # cur_bricks = deepcopy(bricks)
        # 원래는 이차원 행렬을 깊은 복사 하는 deepcopy()라는 함수를 따로 만들었으나
        # 리스트 슬라이싱을 사용하는 깊은 복사로 변경하였다.
        cur_bricks = [b[:] for b in bricks]
        cur_h = 0

        while cur_h < H and not cur_bricks[cur_h][w]:
            cur_h += 1

        num_erase = 0
        if cur_h < H:
            num_erase = erase_bricks(cur_h, w, cur_bricks)
            sort_bricks(cur_bricks)
        dfs(result + num_erase, k + 1, cur_bricks)


for tc in range(int(input())):
    N, W, H = map(int, input().split())
    origin_bricks = [list(map(int, input().split())) for _ in range(H)]

    # 탐색하기 전에 전체 벽돌 수를 세서 num_all_bricks에 저장해둔다.
    num_all_bricks = 0
    for y in range(H):
        for x in range(W):
            if origin_bricks[y][x] != 0:
                num_all_bricks += 1

    max_result = 0
    dfs(0, 0, origin_bricks)

    print('#{} {}'.format(tc + 1, num_all_bricks - max_result))


########################################################################################################


# # 신동호
# # 시간 오래 걸리는 deepcopy 대신 visited라는 새로운 행렬 생성
# from collections import deque
#
#
# def shoot(A, cnt):                                                    # 벽돌 깨는 함수
#     global minimum                                                    # 남은 최소 벽돌 수
#     if cnt:                                                           # 깰 수 있는 기회가 남음
#         for j in range(W):                                            # 모든 위치에서 공 발사
#             visited = [[0] * W for _ in range(H)]                     # 깨졌는지 확인
#             flag = 0                                                  # 현재 열 벽돌 있는지 flag
#             for i in range(H):                                        # 벽돌과 만나는 첫번쨰 높이
#                 if A[i][j]:                                           # 현재 위치에 벽돌이 있다면
#                     q = deque()                                       # 부서지는 벽돌들 q
#                     q.append((i, j))
#                     while q:                                          # 부서질 벽돌 있다면
#                         i, j = q.popleft()
#                         if not visited[i][j]:                         # 아직 안깨진 벽돌
#                             for sh in range(A[i][j]):                 # 범위만큼
#                                 for dd in d:                          # 상하좌우
#                                     si = sh * dd[0] + i
#                                     sj = sh * dd[1] + j
#                                     if si in range(H) and sj in range(W) and not visited[si][sj]: # 범위 안에 있고 안깨졌다면
#                                         q.append((si, sj))            # 깨질 벽돌 추가
#                             visited[i][j] = 1                         # 현재 위치 깨짐 표시
#                     arr = arrange(A, visited)                         # 중력에 의한 정돈
#                     flag = 1                                          # 현재 열 벽돌 있었음
#                     break                                             # 다음 높이 확인할 필요 없음
#             if not flag:                                              # 벽돌이 없었다면
#                 arr = A                                               # 변화 없음
#             shoot(arr, cnt-1)                                         # 기회 1 감소
#     else:                                                             # 기회 다 씀
#         tot = 0                                                       # 남은 벽돌 계산
#         for i in range(H):
#             for j in range(W):
#                 if A[i][j]:
#                     tot += 1
#         if tot < minimum:
#             minimum = tot
#
#
# def arrange(A, visited):                                              # 중력에 의한 정돈 함수
#     arr = [[0] * W for _ in range(H)]                                 # 새로 정돈될 행렬
#     for j in range(W):
#         height = H - 1                                                # 맨 아래부터 벽돌이 쌓인다
#         for i in range(H-1, -1, -1):
#             if not visited[i][j]:                                     # 안 꺠진 벽돌이라면 아래서부터 추가
#                 arr[height][j] = A[i][j]
#                 height -= 1
#     return arr                                                        # 정돈된 행렬 반환
#
#
# T = int(input())
#
# d = [[0, 1], [0, -1], [1, 0], [-1, 0]]                                # 우, 좌, 하, 상
#
# for tc in range(1, T+1):
#     N, W, H = map(int, input().split())
#     mat = [list(map(int, input().split())) for _ in range(H)]
#     minimum = 987654321
#
#     shoot(mat, N)
#     print('#{} {}'.format(tc, minimum))
#
#
# #################################################################################################################
#
#
# # 주영한
# import copy
# directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
#
# # 백트래킹의 재귀를 종료시킬 변수, 현재 벽돌들의 상태를 나타내는 변수, 현재까지 깬 벽돌의 수가 변수로 필요하다.
# # cnt는 구슬을 떨어트린 횟수를 나타내는 변수를 의미
# # now_list는 현재 벽돌의 상태를 나타내는 변수를 의미
# # pop_cnt는 현재까지 깬 벽돌의 수를 나타내는 변수를 의미
#
#
# def backTracking(cnt, now_list, pop_cnt):
#     global max_num
#
#     # 만약 구슬을 N번 떨어트렸다면, 재귀를 종료한다.
#     if cnt == N:
#         # 현재까지 깬 벽돌의 수가 지금까지 확인한 상태 중 최대로 깬 벽돌의 수보다 크면
#         # 이를 업데이트 한다.
#         if max_num < pop_cnt:
#             max_num = pop_cnt
#         return
#
#     # 구슬을 떨어트리는 도중에 다 깬 경우가 발생하면, 더 이상 볼 필요가 없으므로
#     # 확인하지 않는다.
#     if max_num == total_num:
#         return
#
#     # 구슬을 떨어트릴 위치를 for문을 통해 col 변수로 지정하고, 이 지점에 떨어트려본다.
#     for col in range(W):
#         # 구슬을 떨어트렸을 때 생기는 벽돌의 상태를 나타내는 temp_list와
#         # 그 경우 깨게 되는 벽돌의 수를 temp_pop_cnt 변수에 저장한다.
#         temp_list, temp_pop_cnt = getDrop(col, now_list)
#
#         # 구슬을 떨어트렸으므로 cnt + 1와 현재 구슬을 떨어트린 상태와 이번 차례에 깬 벽돌의 수(temp_pop_cnt)를
#         # pop_cnt에 더해주어 함수를 호출한다.
#         backTracking(cnt + 1, temp_list, pop_cnt + temp_pop_cnt)
#     return
#
#
# # 벽돌을 떨어트렸을 때 변화는 상태와 깨게되는 벽돌의 수를 반환하는 함수
# def getDrop(col, now_list):
#     # 새로운 리스트로 형성하여 처리해준다.
#     temp_list = copy.deepcopy(now_list)
#
#     # 이번 차례에 깨트릴 벽돌의 수를 저장할 temp_pop_cnt 변수를 선언한다.
#     temp_pop_cnt = 0
#
#     # 처음으로 맞추게 될 변수 first_strike를 선언한다.
#     # 이때 첫번째 인덱스에는 row의 값, 두번째 인덱스에는 col의 값, 세번째 인덱스에는 벽돌에 새겨진 숫자를 의미한다.
#     first_strike = [0, col, 0]
#     for r in range(H):
#         if temp_list[r][col] > 0:
#             first_strike[0] = r
#             first_strike[2] = temp_list[r][col]
#             temp_list[r][col] = 0
#             temp_pop_cnt += 1
#             break
#
#     # 선형 큐를 선언하여, BFS를 통하여 현재 차례에서 깨지게 되는 모든 벽돌을 깨트린다.
#     front = -1
#     rear = 0
#     queue = [[0, 0, 0]] * (W * H)
#     queue[rear] = first_strike
#
#     while front < rear:
#         # 선형 큐에 대한 pop 연산으로,
#         # temp_row, temp_col는 터진 벽돌의 row, col
#         # bomb_numbers는 터진 벽돌에 새겨진 숫자를 의미한다.
#         front += 1
#         temp_row, temp_col, bomb_numbers = queue[front]
#
#         # 벽돌에 새겨진 숫자 - 1 만큼의 범위를 터트리므로, 이 범위를 bomb_num을 통하여 순회한다.
#         for bomb_num in range(bomb_numbers):
#             for direction in directions:
#                 # bomb_numbers = 4일 경우
#                 # bomb_num = 0, 1, 2, 3으로 순회하며 새로 터트릴 후보가 될 지역의 row와 col을 new_row, new_col에 저장한다.
#                 new_row = temp_row + direction[0] * bomb_num
#                 new_col = temp_col + direction[1] * bomb_num
#
#                 # 터트릴 후보의 벽돌의 변호가 1이면 추가적인 영향을 안끼치므로 깨트린 횟수만 증가시켜주고,
#                 # 번호가 1보다 크면, 선형 큐에 추가해주어 추가적인 폭발을 연산해준다.
#                 if 0 <= new_row < H and 0 <= new_col < W:
#                     if temp_list[new_row][new_col] > 0:
#                         if temp_list[new_row][new_col] == 1:
#                             temp_list[new_row][new_col] = 0
#                         else:
#                             # 선형 큐의 push 연산
#                             rear += 1
#                             queue[rear] = [new_row, new_col, temp_list[new_row][new_col]]
#                             temp_list[new_row][new_col] = 0
#                         temp_pop_cnt += 1
#
#     # 현재 경우에서 깨지게 되는 상황을 모두 확인한 후에 중력을 적용시켜준다.
#     applyGravity(temp_list)
#     return temp_list, temp_pop_cnt
#
#
# def applyGravity(temp_list):
#     for c in range(W):
#         start_row = 0
#         for r in range(H):
#             if temp_list[r][c] == 0:
#                 for row_idx in range(r - 1, start_row - 1, -1):
#                     temp_list[row_idx + 1][c] = temp_list[row_idx][c]
#                     temp_list[row_idx][c] = 0
#                 start_row += 1
#     return
#
#
# # 전체 벽돌의 수를 세는 getTotal 함수
# def getTotal(maps):
#     cnt = 0
#     for r in range(H):
#         for c in range(W):
#             # 벽돌이면, cnt를 하나 증가시킨다.
#             if maps[r][c] > 0:
#                 cnt += 1
#     return cnt
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, W, H = map(int, input().split())
#     maps = [list(map(int, input().split())) for _ in range(H)]
#
#     # 현재 테스트 케이스에 주어진 전체 벽돌의 수를 세어 total_num 변수에 저장한다
#     total_num = getTotal(maps)
#     # 가장 많이 벽돌을 깬 횟수를 저장 할 max_num 변수를 선언한다.
#     max_num = 0
#     # 백트래킹 시작
#     backTracking(0, maps, 0)
#
#     print("#{} {}".format(tc, total_num - max_num))
