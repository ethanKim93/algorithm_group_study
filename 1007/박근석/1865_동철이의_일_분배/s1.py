import sys
sys.stdin = open('input.txt')

T = int(input())

def back_track(now, cnt):
    global max_sum
    if cnt <= max_sum: return

    if now >= N:
        max_sum = max(max_sum, cnt)

    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                back_track(now+1, cnt * (matrix[i][now]/100))
                visited[i] = 0



for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for i in range(N)]
    visited = N*[0]
    max_sum = 0
    back_track(0,1)
    print('#{} {}'.format(tc, format(max_sum*100, '.6f')))


