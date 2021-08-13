import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_total = 0
    for row in range(N - M + 1):
        for col in range(N - M + 1):
            result = 0
            for dr in range(M):
                for dc in range(M):
                    result += arr[row+dr][col+dc]

            if result > max_total:
                max_total = result
    print('#{} {}'.format(tc, max_total))
