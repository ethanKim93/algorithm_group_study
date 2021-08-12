import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maps = list(map(int,input().split()))

    # Selection sort
    for i in range(n):
        mn = 1000000
        for x in range(i,n):
            if mn > maps[x]:
                mn_idx, mn = x, maps[x]
        maps[i], maps[mn_idx] = maps[mn_idx], maps[i]

    print("#{} {}".format(tc, " ".join(map(str,maps))))