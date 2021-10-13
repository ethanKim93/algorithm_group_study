# 한번 폭탄 실행 후 -> 다시 원상복귀 코드 추가예정!!(deepcopy)

import sys
sys.stdin = open('sample_input.txt')


def bomb(i, j, num):
    bombs = []
    bombs.append([i, j, num])

    # 상 하 좌 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    now = bombs.pop(0)
    if now[2] == 1:
        brick[now[0]][now[1]] = 0
        brick_num[now[1]] -= 1
    else:
        for k in range(4):
            move = 0
            while move < now[2]:
                ni = now[0] + di[k]*move
                nj = now[1] + dj[k]*move
                if brick[ni][nj] != 0 and 0 <= ni < H and 0 <= nj < W:
                    bombs.append([ni, nj, brick[ni][nj]])
                    brick[ni][nj] = 0
                move += 1

    while bombs:
        go = bombs.pop(0)
        brick_num[go[1]] -= 1
        bomb(go[0], go[1], go[2])




def break_brick(n):
    global result, H, N

    if n == N:
        if sum(brick_num) < result:
            result = sum(brick_num)
        return

    for j in range(W):
        if H-brick_num[j] != 0 and brick[H-brick_num[j]][j] != 0:
            bomb(H-brick_num[j], j, brick[i][j])
            break

    # gravity
    for y in range(W):
        for x in range(H-1, H-brick_num[y]-2, -1):
            if brick[x][y] == 0:
                brick[x][y], brick[x-1][y] = brick[x-1][y], brick[x][y]

    break_brick(n+1)




T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    brick = [list(map(int, input().split())) for _ in range(H)]
    result = 999999
    brick_num = [0]*W

    for i in range(H):
        for j in range(W):
            if brick[i][j] != 0:
                brick_num[j] += 1

    break_brick(0)
    print(result)

