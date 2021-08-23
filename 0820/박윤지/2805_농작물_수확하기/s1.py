import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    center = N // 2
    ans = 0
    for i in range(0, center+1):
        if not i:
             for j in range(N):
                 ans += farm[center+i][j]
        else:
            for k in range(i, N-i):
                ans += farm[center+i][k]
                ans += farm[center-i][k]
    print('#{} {}'.format(tc, ans))