import sys

sys.stdin = open('input.txt')
T = 10

for tc in range(1, T + 1):
    M = 100
    Num = int(input())
    arr_field = [list(input()) for _ in range(M)]
    max = 0
    N = 1
    for i in range(M):
        N = N + 1
        for k in range(M - N + 1):
            strfind = ''
            for j in range(k, k + N):
                if i < M and j < M and N<M:
                    strfind += arr_field[i][j]

                if strfind == strfind[::-1]:
                    if max < len(strfind):
                        max = len(strfind)

    N = 1
    for i in range(M):
        N = N + 1
        for k in range(M - N + 1):
            strfind = ''
            for j in range(k, k + N):
                if j < M and i < M and N<M :
                    strfind += arr_field[j][i]

                if strfind == strfind[::-1]:
                    if max < len(strfind):
                        max = len(strfind)


    print('#{} {}'.format(tc,max))
