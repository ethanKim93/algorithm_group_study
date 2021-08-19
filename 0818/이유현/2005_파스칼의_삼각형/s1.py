import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pascal = [[0]*(k+1) for k in range(N)]
    pascal[0][0] = 1

    for i in range(1, N):
        for j in range(i+1):
            if j == 0 or j == i:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    print('#{}'.format(tc))
    for row in pascal:
        print(*row)
