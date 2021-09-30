import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    n, m = map(int,input().split())

    for i in range(n):
        if not(m & (1 << i)):
            print("#{} {}".format(tc,"OFF"))
            break
    else:
        print("#{} {}".format(tc,"ON"))