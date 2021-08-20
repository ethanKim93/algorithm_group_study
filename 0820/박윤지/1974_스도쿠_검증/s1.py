import sys
sys.stdin = open('input.txt')

def is_sdoku(arr):
    # 행, 열 검사
    for i in range(9):
        num_row = set()
        num_col = set()
        for j in range(9):
            num_row.add(sdoku[i][j])
            num_col.add(sdoku[j][i])
        if len(num_row) != 9 or len(num_col) != 9:
            return 0
    # 네모 검사
    row = col = 0
    cnt = 1
    while cnt < 10:
        num = set()
        for i in range(row, row+3):
            for j in range(col, col + 3):
                num.add(sdoku[i][j])
        if len(num) != 9:
            return 0
        col = 3 * (cnt % 3)
        row = 3 * (cnt // 3)
        cnt += 1
    return 1


T = int(input())

for tc in range(1, T+1):
    sdoku = []
    for _ in range(9):
        sdoku.append(list(map(int, input().split())))
    print('#{} {}'.format(tc, is_sdoku(sdoku)))

