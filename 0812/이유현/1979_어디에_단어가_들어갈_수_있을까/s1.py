import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        cnt1 = 0
        for j in range(N):
            if arr[i][j] == 0:
                if cnt1 == K:
                    result += 1
                cnt1 = 0
            else:
                cnt1 += 1
        if cnt1 == K:
            result += 1

    for j in range(N):
        cnt1 = 0
        for i in range(N):
            if arr[i][j] == 0:
                if cnt1 == K:
                    result += 1
                cnt1 = 0
            else:
                cnt1 += 1
        if cnt1 == K:
            result += 1

    print('#{} {}'.format(tc, result))
