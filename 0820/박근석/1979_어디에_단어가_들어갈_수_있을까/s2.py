import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(N)]
    ans = 0

    for i in range(N):
        #행을 검사
        cnt_r = 0
        for j in range(N):
            if board[i][j] == 1:
                cnt_r += 1
            else:
                if cnt_r == K:
                    ans += 1
                cnt_r = 0
        #끝까지 가서야 완성이 된 경우
        if cnt_r == K:
            ans += 1

        #열을 검사
        cnt_c = 0
        for j in range(N):
            if board[j][i] == 1:
                cnt_c += 1
            else:
                if cnt_c == K:
                    ans += 1
                cnt_c = 0
        if cnt_c == K:
            ans += 1

    print('#{} {}'.format(tc, ans))

