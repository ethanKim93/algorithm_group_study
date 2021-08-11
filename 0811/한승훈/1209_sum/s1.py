import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_total = 0
    row = col = lu = ru = 0

    for i in range(100):
        lu += arr[i][i]  # 좌 상향 대각선
        ru += arr[i][N-1-i]  # 우 상향 대각선
        for j in range(100):
            row += arr[i][j]  # 행의 합
            col += arr[j][i]  # 열의 합
        if row > max_total:
            max_total = row
        if col > max_total:
            max_total = col
        row = col = 0
    if lu > max_total:
        max_total = lu
    if ru > max_total:
        max_total = ru
    lu = ru = 0
    print('#{} {}'.format(tc, max_total))

