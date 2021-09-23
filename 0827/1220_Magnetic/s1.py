import sys

sys.stdin = open('input.txt')


T = 10
for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for j in range(N):
        r, c = 0, j
        stack = []

        while r < N:
            if not stack and a[r][c] == 1:
                stack.append(1)
            elif stack and a[r][c] == 2:
                cnt += stack.pop()
            r += 1

    print("#{} {}".format(tc, cnt))