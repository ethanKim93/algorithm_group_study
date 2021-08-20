import sys
sys.stdin = open("input.txt")

T = int(input())


def rot_angle(li, l, cnt):  # 배열, 크기, 횟수
    li_1 = [[0] * l for _ in range(l)]
    for c in range(cnt):
        if c == 0:
            for i in range(l):
                for j in range(l):
                    li_1[i][j] = li[l-1-j][i]
        else:
            li_1 = rot_angle(li_1, l, 1)
    return li_1


for tc in range(1, T+1):
    N = int(input())
    board = [list(input().split()) for _ in range(N)]
    board_90 = rot_angle(board, N, 1)
    board_180 = rot_angle(board, N, 2)
    board_270 = rot_angle(board, N, 3)
    print('#{}'.format(tc))
    for k in range(N):
        print(''.join(board_90[k]), ''.join(board_180[k]), ''.join(board_270[k]))




