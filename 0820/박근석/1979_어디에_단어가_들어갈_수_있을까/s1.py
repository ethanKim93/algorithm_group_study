import sys
sys.stdin = open('input.txt')

T = int(input())

def check(board):
    ans = 0
    for i in range(N):
        cnt_r = 0
        for j in range(N):
            if board[i][j] == 1:
                cnt_r += 1
            else:
                if cnt_r == K:
                    ans += 1
                cnt_r = 0
        if cnt_r == K:
            ans += 1

    return ans

for tc in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(N)]
    sum = 0

    sum += check(board)

    new_board = [[-1]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[j][N-i-1] = board[i][j]

    sum += check(new_board)

    print('#{} {}'.format(tc, sum))

