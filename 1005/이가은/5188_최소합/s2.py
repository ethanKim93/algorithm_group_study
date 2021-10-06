# 근석님 코드
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def sum1(x,y,min_sum):
    global ans
    min_sum= min_sum + matrix[x][y]
    if x == N-1 and y == N-1:        #좌표가 오른쪽 아래까지 도달했을 때
        if min_sum < ans:
            ans = min_sum
            return
    else:
        if 0 <= x+1 < N:            #이동한 x좌표가 매트릭스 범위에 포함되면
            sum1(x+1,y,min_sum)
        if 0 <= y+1 < N:            #이동한 y좌표가 매트릭스 범위에 포함되면
            sum1(x,y+1,min_sum)

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for i in range(N)]

    ans = 10*(2*N -1)               #임의의 최대값
    min_sum = 0
    sum1(0,0, min_sum)
    print('#{} {}'.format(tc, ans))