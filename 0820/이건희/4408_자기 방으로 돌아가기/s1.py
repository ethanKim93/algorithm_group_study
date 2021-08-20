import sys

sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maps = [list(map(int,input().split())) for _ in range(n)]
    temps = [0]*200 # 이 부분 이해안감
    for i, x in maps:
        if i > x:
            i, x = x, i

        # 이 부분 이해안감
        if i % 2 != 0:
            i //= 2
        else:
            i = i//2 -1
        if x % 2 != 0:
            x //= 2
        else:
            x = x//2 -1

        for y in range(i,x+1):
            temps[y] += 1

    mx = 0
    for i in temps:
        if i > mx:
            mx = i

    print("#{} {}".format(tc, mx))