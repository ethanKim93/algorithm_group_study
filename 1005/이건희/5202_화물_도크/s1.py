import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maps = []
    for i in range(n):
        maps.append(list(map(int,input().split())))

    maps = sorted(maps, key=lambda x: x[1])
    cnt = 0
    pre_e = 0
    while maps:
        s, e = maps.pop(0)
        if pre_e <= s:
            cnt += 1
            pre_e = e

    print("#{} {}".format(tc, cnt))