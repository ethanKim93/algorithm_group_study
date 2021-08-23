import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    ans = 0
    plus = len(farm)//2
    minus = len(farm)//2
    for i in range(N):
        for j in range(plus, minus+1):
            ans += farm[i][j]
        if i < len(farm)//2:
            plus -= 1
            minus += 1
        else:
            plus += 1
            minus -= 1

    print('#{} {}'.format(tc, ans))