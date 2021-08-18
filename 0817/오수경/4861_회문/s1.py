import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    # 가로
    for i in board:
        a = 0
        while a + M <= len(i):
            if i[a:a+M] == i[a:a+M][-1::-1]:
                print('#{} {}'.format(tc, "".join(i[a:a+M])))
                a += 1
            else:
                a += 1

    # 세로

    for i in range(N):
        for j in range(N):
            if i < j:
                board[i][j], board[j][i] = board[j][i], board[i][j]

    for i in board:
        a = 0
        while a + M <= len(i):
            if i[a:a+M] == i[a:a+M][-1::-1]:
                print('#{} {}'.format(tc, "".join(i[a:a+M])))
                a += 1
            else:
                a += 1