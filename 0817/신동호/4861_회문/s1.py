import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int,input().split()))
    strings = [input() for _ in range(N)]
    result = ''
    for i in range(N-M+1):
        for j in range(N-M+1):
            for k in range(M):
                for x in range(M//2):
                    if strings[i+k][j+x] != strings[i+k][j+M-x-1]:
                        break
                else:
                    result = strings[i+k][j:j+M]

                for y in range(M//2):
                    if strings[i+y][j+k] != strings[i+M-y-1][j+k]:
                        break
                else:
                    col = ''
                    for p in range(i, i+M):
                        col = col + strings[p][j+k]
                    result = col
    print('#{} {}'.format(tc, result))

    #
    # for I in range(N-M+1):
    #     for J in range(N-M+1):
    #         for a in range(M):
    #             for b in range(M):
    #                 i = I+a
    #                 j = J+b
    #                 par1 = par2 = 0
    #                 for x in range(M//2):
    #                     print(strings[i][j+x], strings[i][j+M-x-1])
    #                     if strings[i][j+x] != strings[i][j+M-x-1]:
    #                         par1 = 1
    #                     if strings[i+x][j] != strings[i+M-x-1][j]:
    #                         par2 = 1
    #             if not par1:
    #                 print(strings[i][j:j+M])
    #             elif not par2:
    #                 print(strings[i:i+M][j])
    # print(tc)
