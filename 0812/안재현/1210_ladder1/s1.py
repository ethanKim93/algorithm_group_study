# 안되는거

import sys

sys.stdin = open('input.txt')

for tc in range(0, 10):
    T = int(input())
    N = 100
    A = [list(map(int, input().split())) for _ in range(N)]
    # for i in range(0, 100):
    # #     print(A)
    # #     print(A[1])
    # # print(T)
    # print(A[0][0])
    k = 0
    j = 99
    a = []
    switch = 0
    # for i in range(100):    # i는 가로 j는 세로
    for i in range(0, 100):
        if A[99][i] == 2:
            print(j, i)
            k = i
            while j >= 0:
                if k == 0:
                    if A[j][k + 1] == 1:
                        k += 1
                        while A[j][k + 1] == 0:
                            k += 1
                        j -= 1
                        print('오른쪽으로1')
                    elif A[j - 1][k] == 1:
                        j -= 1
                        print('아래로1')
                    else:
                        print('종료1')
                        print(j, k)
                        print()
                        break
                elif k == 99:
                    if A[j][k - 1] == 1:
                        k -= 1
                        while A[j][k - 1] == 0:
                            k -= 1
                        j -= 1
                        print('왼쪽으로2')
                    elif A[j - 1][k] == 1:
                        j -= 1
                        print('아래로2')
                    else:
                        print('종료2')
                        print(j, k)
                        print()
                        break
                else:
                    if A[j][k-1] == 1:
                        k -= 1
                        while A[j][k-1] == 0:
                            k -= 1
                            if k == 0:
                                break
                        j -= 1
                        print('왼쪽으로3')
                    if A[j][k+1] == 1:
                        k += 1
                        while A[j][k+1] == 0:
                            k += 1
                            if k == 99:
                                break
                        j -= 1
                        print('오른쪽으로3')
                    elif A[j-1][k] == 1:
                        j -= 1
                        print('아래로3')
                    else:
                        print('종료3')
                        print(j, k)
                        print()
                        break

    # while a[1] != 0:
    #     if A[a[1]][a[0]] == 2:
    #         a[1] -= 1
    #     elif A[a[1]][a[0]] == 1:
    #         if not A[a[1]][a[0] + 1] or not A[a[1]][a[0] - 1]:
    #             a[1] -= 1
    #         elif A[a[1]][a[0] + 1] == 1:
    #             while A[a[1]][a[0]+1] == 0:
    #                 a[0] += 1
    #             a[1] -= 1
    #         elif A[a[1]][a[0] - 1] == 1:
    #             while A[a[1]][a[0]-1] == 0:
    #                 a[0] -= 1
    #             a[1] -= 1
    #         elif A[a[1] - 1][a[0]] == 1:
    #             a[1] -= 1
    #         elif not A[a[1]-1][a[0]]:
    #             print(i, a[1])