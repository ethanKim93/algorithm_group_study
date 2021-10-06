import sys
sys.stdin = open('input.txt')

T = int(input())

def sum1(x,y,min):
    global ans
    min = min + matrix[x][y]
    if x == N-1 and y == N-1:
        if min < ans:
            ans = min
            return
    else:
        if 0 <= x+1 < N:
            sum1(x+1,y,min)
        if 0 <= y+1 < N:
            sum1(x,y+1,min)

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for i in range(N)]

    ans = 10*(2*N -1)
    min = 0
    sum1(0,0, min)
    print('#{} {}'.format(tc, ans))

