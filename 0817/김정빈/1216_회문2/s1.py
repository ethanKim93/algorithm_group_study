import sys
sys.stdin = open("input.txt")

def is_pal(x):
    if len(x) > 1:
        if x[0] == x[-1]:
            return is_pal(x[1:-1])
    else:
        return True
def check(arr, N, M):
    for i in range(N):
        for j in range(N - M + 1):
            row = ''
            col = ''
            for k in range(M):
                row += arr[i][j + k]
                col += arr[j + k][i]
            if is_pal(row):
                return row
            if is_pal(col):
                return col
    return False

for tc in range(1, 11):
    T = int(input())
    arr = [list(input()) for _ in range(100)]
    N = 100

    for M in range(N, 1, -1):
        if check(arr, N, M):
            print('#{} {}'.format(tc, M))
            break

    # print('#{} {}'.format(tc, res))
    #     print('#{} {}'.format(tc, check(arr, N, M)))