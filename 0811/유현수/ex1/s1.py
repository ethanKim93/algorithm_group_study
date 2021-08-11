import sys
sys.stdin=open('input.txt')

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]

    result = 0
    for r in range(N):
        for c in range(N):
            total = 0
            for i in range(4):
                idx_r = r + dr[i]
                idx_c = c + dc[i]
                if 0 <= idx_r < N and 0 <= idx_c < N:
                    temp = arr[r][c] - arr[idx_r][idx_c]
                else:
                    temp = 0
                if temp >= 0:
                    total += temp
                else:
                    total += -temp
            result += total

    print('#{} {}'.format(tc, result))