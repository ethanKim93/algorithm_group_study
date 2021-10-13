# juan, 주영한, 신동호님 코드 참고해서 풀기
# juan 교수님 코드 따라씀
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def gravity(arr):
    for c in range(W):
        s = []  # stack
        for r in range(H):
            if arr[r][c]:
                s.append(arr[r][c])
                arr[r][c] = 0
        h = H-1
        while s:
            arr[h][c] = s.pop()
            h -= 1


def shot(row, col, new_arr):
    stack = [(row, col)]
    while stack:
        r, c = stack.pop()  # pop()은 마지막 요소를 꺼낸다
        if new_arr[r][c] > 1:
            for i in range(4):  # 방향 정하기
                nr, nc = r + dr[i], c + dc[i]
                for _ in range(new_arr[r][c]-1):
                    if 0 <= nr < H and 0 <= nc < W:
                        if new_arr[nr][nc] > 1:
                            stack.append((nr, nc))  # 스택에 넣어서 while문 또 돌게끔
                        else:
                            new_arr[nr][nc] = 0
                        nr, nc = nr + dr[i], nc + dc[i]  # new_arr[r][c]이 2 이상이면 그만큼 더 봐야함
                    else:
                        break
        new_arr[r][c] = 0
    gravity(new_arr)


def remain(arr):
    cnt = 0
    for c in range(0, W):
        for r in range(H-1, -1, -1):
            if arr[r][c] == 0:
                break
            cnt += 1
    return cnt


def dfs(idx, arr):
    global bricks
    if not bricks:  # 구슬을 N번 쏘기 전에 남은 벽돌이 0일 때
        return
    if idx == N:
        res = remain(arr)
        if res < bricks:
            bricks = res
        return

    for c in range(W):  # 구슬의 열
        new_arr = [list(arr[_]) for _ in range(H)]  # ???????? arr을 깊은복사함
                                                    # 구슬을 던질때마다 새로운 리스트로 만듦
                                                    # (구슬을 다른데다 던질 경우로 돌아갔을 때 맞는 시기 arr 쓸 수 있도록)
        for r in range(H):  # 그 열의 맨위 벽돌 찾아냄
            if new_arr[r][c]:
                shot(r, c, new_arr)
                if not remain(new_arr):  # 구슬 투하 후 남은 벽돌 있는지 확인
                    bricks = 0
                    return
                dfs(idx+1, new_arr)  # 남은 벽돌 있으면 다시 구슬 던짐
                break  # 맨 위 벽돌만 보면 되고, 다봤으면 다음 열로 넘어가야하기에 break


for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    base = [list(map(int, input().split())) for _ in range(H)]
    bricks = 987654321
    dfs(0, base)
    print('#{} {}'.format(tc, bricks))


########################################################
# # 내가 풀다 만 거...
# # 벽돌들 깨트릴 때 b1함수를 재귀호출 하는 코드인데, 풀릴 수 있지만 stack으로 하는 게 낫다
# # 수습 해보려고 했는데 b1 재귀호출 할 때 인덱스까지 범위 확인해야해서 포기함
# import sys
# sys.stdin = open('sample_input.txt')
#
# import copy
#
#
# def grav(arr):
#     # 떠있는 벽돌들 아래로 내리기
#     f0r = N
#     for n in range(W - 1, -1, -1):
#         for o in range(H - 1, -1, -1):
#             if f0r == N and arr[n][o] == 0:
#                 f0r = o
#             if arr[n][o] != 0 and f0r != N:
#                 arr[n][f0r] = arr[n][o]
#                 arr[n][o] = 0
#                 f0r = o - 1
#     return arr
#
#
# def b1(i, j, v, arr):  # i, j: 행, 열 좌표, v: brick[i][j], arr: 들어온 배열
#     # 폭탄 터트리기
#     if v == 0 or i < 0 or i >= H or j < 0 or j >= W:
#         return
#     if v == 1:
#         arr[i][j] = 0
#         return arr
#     else:
#         arr[i][j] = 0
#         for m in range(-(v-1), (v-1)+1):
#             # list index out of range
#             b1(i+m, j, arr[i+m][j], arr)
#             b1(i-m, j, arr[i-m][j], arr)
#             b1(i, j+m, arr[i][j+m], arr)
#             b1(i, j-m, arr[i][j-m], arr)
#         return grav(arr)
#
#
# def remain(arr):
#     cnt1 = 0
#     for r in range(0, W):
#         for s in range(H-1, -1, -1):
#             if arr[s][r] == 0:
#                 break
#             cnt1 += 1
#     return cnt1
#
#
# def select(arr, cnt):
#     global ans
#     if cnt == N:
#         # arr의 벽돌수를 세고 ans와 비교
#         total = remain(arr)
#         if ans > total:
#             ans = total
#     else:
#         # arr = copy.deepcopy(arr1)
#         new_arr = [list(arr[_]) for _ in range(H)]
#         for q in range(0, W):
#             for l in range(0, H):
#                 if new_arr[l][q]:
#                     ir = l
#                     select(b1(ir, q, new_arr[ir][q], new_arr), cnt+1)
#                     break
#             else:
#                 return
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, W, H = map(int, input().split())
#     brick = [list(map(int, input().split())) for _ in range(H)]
#     ans = 987654321
#     select(brick, 0)
#     print(ans)
#     # if N == 1:
#     #     for i in range(0, W):
#     #         select(i, brick)
