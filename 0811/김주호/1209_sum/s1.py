import sys
sys.stdin = open("input.txt")

for case in range(10):
    C = int(input())
    li = []
    for _ in range(100):
        li.append(list(map(int, input().split())))

    total_row = 0
    total_col = 0
    sum_ltrb = 0
    sum_lbrt = 0

    for i in range(100):
        sum_row = 0
        sum_col = 0
        for j in range(100):
            sum_row += li[i][j]
            sum_col += li[j][i]
            if i == j:
                sum_ltrb += li[i][j]
            if i + j == 99:
                sum_lbrt += li[i][j]

        if total_row < sum_row:
            total_row = sum_row
        if total_col < sum_col:
            total_col = sum_col

    print("#{} {}".format(C, max(total_col, total_row, sum_ltrb, sum_lbrt)))