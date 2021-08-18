import sys

sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    print("#" + str(tc))
    print(1)
    alist = [1]
    blist = []
    for i in range(n - 1):
        blist = []
        blist.append(1)
        for x in range(len(alist) - 1):
            blist.append(alist[x] + alist[x + 1])
        blist.append(1)
        print(*blist)
        alist = blist
