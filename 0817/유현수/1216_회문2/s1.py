import sys
sys.stdin = open('input.txt')


def is_pal(x):
    left = 0
    right = len(x)-1
    while left < right:
        if x[left] == x[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def check(board, N):
    for i in range(100):
        for j in range(100-N+1):
            row = ''
            col = ''
            for k in range(N):
                row += board[i][j+k]
                col += board[j+k][i]
            if is_pal(row):
                return N
            if is_pal(col):
                return N
    return 0


for _ in range(10):
    T = int(input())
    board = [list(input()) for _ in range(100)]
    result = 0
    for N in range(3, 101):
        tmp = check(board, N)
        if result < tmp:
            result = tmp
    print('#{} {}'.format(T, result))
