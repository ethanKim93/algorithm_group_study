import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, list(input()))) for _ in range(N)]
    profit = 0
    i = 0
    j = N//2
    r = 1
    while i < N:
        for k in range(r):
            profit += farm[i][j + k]
        i += 1
        if i <= N//2:
            j -= 1
            r += 2
        else:
            j += 1
            r -= 2
    print('#{} {}'.format(tc, profit))