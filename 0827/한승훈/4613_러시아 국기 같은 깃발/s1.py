import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    min_val = N * M

    w_cnt = 0
    for w in range(0, N-2):
        for m in range(M):
            if flag[w][m] != 'W':
                w_cnt += 1
        b_cnt = 0
        for b in range(w+1, N-1):
            for m in range(M):
                if flag[b][m] != 'B':
                    b_cnt += 1
            r_cnt = 0
            for r in range(b+1, N):
                for m in range(M):
                    if flag[r][m] != 'R':
                        r_cnt += 1
            if (w_cnt + b_cnt + r_cnt) < min_val:
                min_val = (w_cnt + b_cnt + r_cnt)
    print('#{} {}'.format(tc, min_val))







