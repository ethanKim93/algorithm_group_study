import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1,t+1):
    n, xint = input().split()
    n = int(n)
    xdic = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
    ans = ""
    for i in range(n):
        temps = ""
        if xint[i] in list(str(j) for j in range(10)):
            for x in range(4):
                if int(xint[i]) & (1<<x):
                    temps = "1" + temps
                else:
                    temps = "0" + temps

        else:
            for x in range(4):
                if xdic[xint[i]] & (1<<x):
                    temps = "1" + temps
                else:
                    temps = "0" + temps

        ans = ans + temps

    print("#{} {}".format(tc, ans))