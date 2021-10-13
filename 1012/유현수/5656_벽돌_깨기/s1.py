import sys
sys.stdin = open('sample_input.txt')

import copy


def get_r_idx(c_idx, arr):
    for i in range(H):
        if arr[i][c_idx]:
            return i
    return -1


def boom(r, c, arr):
    if not arr[r][c]:
        pass
    elif arr[r][c] == 1:
        arr[r][c] = 0
    else:
        explosion = arr[r][c]
        arr[r][c] = 0
        for i in range(4):
            for j in range(1, explosion):
                nr = r + dr[i] * j
                nc = c + dc[i] * j
                if 0 <= nr < H and 0 <= nc < W:
                    boom(nr, nc, arr)


def gravity(arr):
    for c in range(W):
        start_row = 0
        for r in range(H):
            if arr[r][c] == 0:
                for row_idx in range(r - 1, start_row - 1, -1):
                    arr[row_idx + 1][c] = arr[row_idx][c]
                    arr[row_idx][c] = 0
                start_row += 1
    return


def gravity2(arr):
    for c in range(W):
        s = []
        for r in range(H):
            if arr[r][c]:               # 숫자가 들어있는 벽돌을
                s.append(arr[r][c])     # 스택에 넣고
                arr[r][c] = 0           # 해당 위치는 0으로
        h = H-1
        while s:
            arr[h][c] = s.pop()         # 스택에서 하나씩 꺼내서 해당 열의 바닥부터 다시 채워 올림
            h -= 1


def count_bricks(arr):
    cnt = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                cnt += 1
    return cnt


def shoot(c_idx, N, arr):
    global ans
    if N == 0:
        bricks_cnt = count_bricks(arr)
        if ans > bricks_cnt:
            ans = bricks_cnt
        return 0
    else:
        tmp = copy.deepcopy(arr)            # 현재 벽돌 상태 저장
        r_idx = get_r_idx(c_idx, tmp)       # 가장 위에 있는 벽돌의 행 인덱스
        if r_idx == -1:                     # 해당 열이 비어있으면 return
            return 1
        boom(r_idx, c_idx, tmp)             # 폭발!
        gravity2(tmp)                        # 중력 적용
        flag = 0
        for i in range(W):                  # 폭발된 상태에서 다시 shoot
            flag += shoot(i, N-1, tmp)
        if flag == W:
            ans = 0
        return 0


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]

    ans = 987654321
    for i in range(W):
        shoot(i, N, bricks)
    print('#{} {}'.format(tc, ans))
