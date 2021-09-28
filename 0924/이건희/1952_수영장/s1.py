import sys
sys.stdin = open("input.txt")

def BF(month, price):
    global ans
    if month > 12:
        ans = min(ans, price)
        return

    BF(month+1, price+maps[month]*d)
    BF(month+1, price+m1)
    BF(month+3, price+m3)

for tc in range(1, int(input())+1):
    d, m1, m3, y = map(int,input().split())
    maps = [0] + list(map(int,input().split()))
    ans = y
    BF(1,0)

    print("#{} {}".format(tc,ans))

# Pass