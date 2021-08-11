import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = M = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for i in range(N):
        for j in range(M):
            sum_abs = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    value_abs = arr[i][j] - arr[ni][nj]
                    if value_abs >= 0:
                        sum_abs += value_abs
                    else:
                        sum_abs -= value_abs
            result += sum_abs
    print('#{} {}'.format(tc, result))


