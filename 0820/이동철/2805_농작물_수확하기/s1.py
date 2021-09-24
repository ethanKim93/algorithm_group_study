import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        idx = abs(i - (N // 2))
        arr = farm[i][idx:N - idx]
        for j in arr:
            cnt += j
    print('#{} {}'.format(tc, cnt))
