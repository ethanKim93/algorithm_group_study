import sys
sys.stdin = open("input.txt")

def check(somelist):
    for i in range(10):
        if somelist[i] >= 3:
            return 1
    for i in range(8):
        if somelist[i]:
            if somelist[i+1] and somelist[i+2]:
                return 1
    return False

t = int(input())
for tc in range(1,t+1):
    maps = list(map(int,input().split()))
    alist = [0]*10
    blist = [0]*10
    ans = 0
    for i in range(0,12,2):
        alist[maps[i]] += 1
        blist[maps[i+1]] += 1

        if i >= 4:
            result1 = check(alist)
            result2 = check(blist)
            if result1 or result2:
                if result1 == result2:
                    ans = 1
                elif result1:
                    ans = 1
                elif result2:
                    ans = 2
                break

    print("#{} {}".format(tc, ans))

# Pass