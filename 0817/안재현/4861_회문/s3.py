import sys

sys.stdin = open('sample_input.txt', 'rt', encoding='UTF8')

T = int(input())

def is_pal(x):
    if len(x) > 1:
        if x[0] == x[-1]:
            return is_pal(x[1:-1])
    else:
        return False


def check(board, N, M):
    for i in range(N):
        for j in range(N-M+1):
            row = ''
            col = ''
            for k in range(M):
                row += board[i][j+k]
                col += board[j+k][i]
            if is_pal(row):
                return row
            if is_pal(col):
                return col


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    print('#{} {}'.format(tc, check(board, N, M)))
