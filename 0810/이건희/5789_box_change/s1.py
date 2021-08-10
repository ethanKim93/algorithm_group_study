import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    n, q = map(int,input().split())
    maps = [0] * n
    for i in range(1,q+1):
        l,r = map(int, input().split())
        for x in range(l-1,r):
            maps[x] = i

    print("#{} {}".format(tc, " ".join(map(str, maps))))