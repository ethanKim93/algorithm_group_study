import sys
sys.stdin = open("input.txt")

def permutation(k):
    global route_temps, ans

    if k == n-1:
        temps = [0] + route_temps + [0]
        subans = 0
        for i in range(len(temps)-1):
            subans += maps[temps[i]][temps[i+1]]
            if subans >= ans:
                break
        if subans < ans:
            ans = subans
        return

    for i in range(len(route_temps)):
        if not route_temps[i]:
            route_temps[i] = route[k] - 1
            permutation(k+1)
            route_temps[i] = 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maps = [list(map(int,input().split())) for _ in range(n)]
    route = [i for i in range(2, n+1)]
    route_temps = [0]*(n-1)
    route_list = []
    ans = 10000
    permutation(0)

    print("#{} {}".format(tc,ans))