
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
    j = 99
    # for i in range(100):    # i는 가로 j는 세로
    for i in range(0, 100):
        if A[99][i] == 2:
            # print(i)
            while j != 0:
                if A[j][i] == 2:
                    j -= 1
                elif A[j][i] == 1:
                    if A[j][i + 1] == 1:
                        i += 1
                    elif A[j][i - 1] == 1:
                        i -= 1
                    elif A[j - 1][i] == 1:
                        j -= 1
    print(j)