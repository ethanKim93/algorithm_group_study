import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # N = 행, M = 열
    arr = [list(input()) for _ in range(N)]

    total = N * M
    w_result = 0
    for w in range(0, N - 2):
        for c in range(0, M):
            if arr[w][c] != 'W':
                w_result += 1
        r_result = 0
        for b in range(w + 1, N - 1):
            for c in range(0, M):
                if arr[b][c] != 'B':
                    r_result += 1
            b_result = 0
            for r in range(b + 1, N):
                for c in range(0, M):
                    if arr[r][c] != 'R':
                        b_result += 1

            result = w_result + r_result + b_result
            if total > result:
                total = result
    print('#{} {}'.format(tc, total))

