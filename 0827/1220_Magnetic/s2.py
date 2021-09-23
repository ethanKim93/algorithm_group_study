import sys

sys.stdin = open('input.txt')

for tc in range(1, 10 + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for x in range(N):
        check = 0
        for y in range(N):
            if check == 0 and MAP[y][x] == 1:
                check = 1
            if check == 1 and MAP[y][x] == 2:
                check = 0
                ans += 1

    print("#{} {}".format(tc, ans))
