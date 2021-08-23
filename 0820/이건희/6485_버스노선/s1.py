import sys

sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maps = []
    stops = []
    for i in range(n):
        maps.append(list(map(int,input().split())))
    p = int(input())
    for i in range(p):
        stops.append(int(input()))
    stops_cnt = [0]*p

    for i, x in maps:
        for y in range(p):
            if i <= stops[y] <= x:
                stops_cnt[y] += 1

    print("#{} {}".format(tc," ".join(map(str,stops_cnt))))