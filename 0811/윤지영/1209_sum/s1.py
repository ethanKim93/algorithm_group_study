T = 10
import sys
sys.stdin = open('input.txt')


for tc in range(1, T+1):
    tc = int(input())
    N = 100
    num_li = []
    for _ in range(N):
        num_li. append(list(map(int,input().split())))

    # 대각선 합
    sum_dia = sum_dia_r = 0
    for i in range(N):
        sum_dia += num_li[i][i]
        sum_dia_r += num_li[i][N-1-i]
    max_li = sum_dia
    if max_li < sum_dia_r:
        max_li = sum_dia_r

    # 행,열 합
    for i in range(N):
        sum_dia = sum_dia_r = 0
        for j in range(N):
            sum_dia += num_li[i][j]
            sum_dia_r += num_li[j][i]
        if sum_dia < sum_dia_r:     # 두 개 크기 먼저 비교한 다음에 최대값 찾기!
            sum_dia = sum_dia_r
        if max_li < sum_dia:
            max_li = sum_dia

    print('#{} {}'.format(tc, max_li))