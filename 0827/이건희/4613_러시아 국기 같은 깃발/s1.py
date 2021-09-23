import sys

sys.stdin = open("input.txt")


def BF(white, blue):
    global ans
    cnt = 0
    for i in range(r):
        for x in range(c):
            if i <= white:
                if maps[i][x] != 'W':
                    cnt += 1
            elif i <= blue:
                if maps[i][x] != 'B':
                    cnt += 1
            else:
                if maps[i][x] != 'R':
                    cnt += 1

    if ans > cnt:
        ans = cnt


t = int(input())
for tc in range(1, t + 1):
    r, c = map(int, input().split())
    ans = 10000
    maps = [list(input()) for _ in range(r)]
    for white in range(0, r - 2):
        for blue in range(white + 1, r - 1):
            BF(white, blue)

    print("#{} {}".format(tc,ans))
