import sys
sys.stdin = open("input.txt")

def BF(k):
    global ans

    if k >= n:
        subans = 0
        for i in range(n):
            subans += temps[i]
            if subans >= ans:
                return
        ans = subans
        return


    for i in range(n):
        flag = False
        if not temps[i]:
            temps[i] = maps[i][k]
            subans = 0
            for x in range(n):
                subans += temps[x]
                if subans >= ans:
                    temps[i] = 0
                    flag = True
                    break
            if flag:
                continue
            BF(k+1)
            temps[i] = 0


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maps = [list(map(int,input().split())) for _ in range(n)]
    temps = [0]*n
    ans = 1000
    BF(0)
    print("#{} {}".format(tc, ans))

# Pass