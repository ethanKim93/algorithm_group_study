import sys
sys.stdin = open('input.txt')

T = int(input())
pascal = [[0] * 10 for _ in range(10)]

for i in range(10):
    for j in range(i+1):
        if j == 0 or i == j:
            pascal[i][j] = 1

        else:
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]


for tc in range(1, T+1):
    N = int(input())
    print('#{}'.format(tc))

    for i in range(N):
        for j in range(i+1):
            print(pascal[i][j], end=' ')
        print()
