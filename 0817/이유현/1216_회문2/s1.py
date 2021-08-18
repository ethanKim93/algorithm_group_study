import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    tc = int(input())
    N = 100
    result = 1

    #가로줄 확인
    row_lst = []
    for i in range(N):
        pal = input()
        row_lst.append(pal)
        #회문 길이
        for M in range(N, result, -1):
            if result > M:
                break
            for k in range(N-M+1):
                if pal[k:M+k] == pal[k:M+k][::-1]:
                    if len(pal[k:M+k]) > result:
                        result = len(pal[k:M+k])

    #세로줄 확인
    col_lst = []
    col_sub_lst = ''
    for x in range(N):
        for y in row_lst:
            col_sub_lst += y[x]
        col_lst.append(col_sub_lst)
        col_sub_lst =''

    for col_pal in col_lst:
        for M in range(N, result, -1):
            if result > M:
                break
            for k in range(N-M+1):
                if col_pal[k:M+k] == col_pal[k:M+k][::-1]:
                    if len(col_pal[k:M+k]) > result:
                        result = len(col_pal[k:M+k])

    print('#{} {}'.format(tc, result))