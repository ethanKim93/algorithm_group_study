import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, list(input()))) for _ in range(N)]
    result = 0
    for i in range(N):
        add = (N//2) - abs(N // 2 - i)
        # print(add)
        for j in range((N//2)-add,(N//2)+add+1):
            # print(i,j,add)
            result += farm[i][j]
    print('#{} {}'.format(tc,result))
