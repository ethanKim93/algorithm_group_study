import sys
sys.stdin = open('input.txt')
from pprint import pprint

Testcase = 10
for tc in range(1, Testcase+1):
    N = int(input())
    T = [list(input()) for _ in range(100)]
    Tcol = [[T[i][j] for i in range(100)] for j in range(100)] # 열 정렬
    # print(T)
    # print(Tcol)
    cnt = 100
    flag = False
    while cnt >= 1:
        for i in range(100-cnt+1):
            for j in range(100-cnt+1):
                if T[i][j:j+cnt] == T[i][j:j+cnt][::-1]:
                    flag = True
                if Tcol[i][j:j+cnt] == Tcol[i][j:j+cnt][::-1]:
                    flag = True
        if flag:
            break
        cnt -= 1
    print('#{} {}'.format(tc, cnt))