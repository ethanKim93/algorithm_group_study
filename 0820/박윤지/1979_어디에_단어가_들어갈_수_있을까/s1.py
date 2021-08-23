import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        blank = 0
        for j in range(N):
            if arr[i][j] == 1:
                blank += 1
                if j == N-1:
                    if blank == K:
                        ans += 1
            else:
                if blank == K:
                    ans += 1
                blank = 0

        cnt_c = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt_c += 1
                if j == N - 1:  # 여기 i 아니고 j여야함
                    if cnt_c == K:
                        ans += 1
            else:
                if cnt_c == K:
                    ans += 1
                cnt_c = 0

    print('#{} {}'.format(tc, ans))
