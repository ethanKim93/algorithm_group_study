def DF(k):
    global ans
    if k == n:
        subans = 1
        for i in range(n):
            subans *= temps[i] * 0.01
            if subans < ans:
                return
        ans = subans
        return

    for i in range(n):
        flag = False
        subans = 1
        if temps[i] == -1:
            temps[i] = maps[i][k]
            for x in range(n):
                if temps[x] != -1:
                    subans *= temps[x]
                    if subans < ans:
                        flag = True
                        break
            if flag:
                continue

            DF(k + 1)
            temps[i] = -1


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]

    ans = 0.01
    temps = [-1] * n
    DF(0)
    print("#" + str(tc) + " {0:.6f}".format(ans * 100))

# Fail: Time over