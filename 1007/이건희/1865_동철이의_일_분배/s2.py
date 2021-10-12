import sys
sys.stdin = open("input.txt")

def DF(k,subans):
    global ans
    if subans < ans:
        return

    if k == n:
        if subans > ans:
            ans = subans
        return

    for i in range(n):
        if temps[i] == -1:
            temps[i] = 1
            DF(k+1, subans*maps[i][k]*0.01)
            temps[i] = -1

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    maps = [list(map(int,input().split())) for _ in range(n)]

    ans = 0.01
    temps = [-1] * n
    DF(0,1)
    print("#" + str(tc) + " {0:.6f}".format(ans*100))

# Pass