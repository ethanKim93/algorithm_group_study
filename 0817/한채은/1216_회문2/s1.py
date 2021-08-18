import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    tc = int(input())
    N = 100
    result = 1

    # 가로줄 확인
    row = []
    for i in range(N):
        r = input()
        row.append(r)
        # 회문 길이
        for M in range(N, result, -1):
            if result > M:
                break
            for k in range(N-M+1):
                if r[k:M+k] == r[k:M+k][::-1]:
                    if len(r[k:M+k]) > result:
                        result = len(r[k:M+k])

    # 세로줄 확인
    column = []
    column_sub_lst = ''
    for x in range(N):
        for y in row:
            column_sub_lst += y[x]
        column.append(column_sub_lst)
        column_sub_lst =''

    for c in column:
        for M in range(N, result, -1):
            if result > M:
                break
            for k in range(N-M+1):
                if c[k:M+k] == c[k:M+k][::-1]:
                    if len(c[k:M+k]) > result:
                        result = len(c[k:M+k])

    print("#{} {}".format(tc, result))
