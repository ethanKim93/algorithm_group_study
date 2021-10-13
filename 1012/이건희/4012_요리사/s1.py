import sys
sys.stdin = open("input.txt")

def cal(temps):
    f1 = f2 = 0
    for i in range(n-1):
        for x in range(i,n):
            if temps[i] and temps[x]:
                f1 += maps[i][x] + maps[x][i]
            elif not temps[i] and not temps[x]:
                f2 += maps[i][x] + maps[x][i]
    return abs(f1-f2)

def check(k, cnt):
    global mn

    if k >= n:
        return

    if cnt == n//2:
        mn = min(mn,cal(temps))

    for i in [1,0]:
        temps[k] = i
        check(k+1,cnt+i)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maps = [list(map(int,input().split())) for _ in range(n)]
    temps = [0] * n
    mn = 987654321
    check(0, 0)
    print("#{} {}".format(tc, mn))

# Pass