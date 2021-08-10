import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    n, m = map(int,input().split())
    maps = list(map(int,input().split()))
    mx = 0
    mn = 1000000
    for i in range(0,n-m+1):
        sm = 0
        for x in range(m):
            sm += maps[i+x]

        if sm > mx:
            mx = sm
        if sm < mn:
            mn = sm

    print("#{} {}".format(tc, mx-mn))