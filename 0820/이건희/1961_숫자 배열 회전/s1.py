import sys

sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    maps = [input().split() for _ in range(n)]
    maps_90 = []
    maps_180 = []
    maps_270 = []
    for i in range(n):
        for x in range(-1, -n - 1, -1):
            maps_90.append(maps[x][i])

    for i in range(-1,-n-1,-1):
        for x in range(-1,-n-1,-1):
            maps_180.append(maps[i][x])

    for i in range(-1,-n-1,-1):
        for x in range(n):
            maps_270.append(maps[x][i])

    print("#" + str(tc))
    ans = []
    for i in range(n):
        ans.append(maps_90[n*i:n*(i+1)])
        ans.append(maps_180[n*(i):n*(i+1)])
        ans.append(maps_270[n*(i):n*(i+1)])

    cnt = 0
    for i in range(n):
        for x in range(3):
            print("".join(ans[cnt]), end=" ")
            cnt += 1
        print()