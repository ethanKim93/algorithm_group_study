import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    rc = []
    li = [[0] * 10 for _ in range(10)]
    for i in range(N):
        r1, c1, r2, c2, color1 = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                li[r][c] += color1
    cnt = 0
    for r in range(10):
        for c in range(10):
            if li[r][c] == 3:
                cnt += 1
    print('#{} {}'.format(tc, cnt))


