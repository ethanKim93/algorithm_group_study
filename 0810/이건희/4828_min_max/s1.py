import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    nums = list(map(int,input().split()))
    mx = 0
    mn = 1000000

    for num in nums:
        if num > mx:
            mx = num

        if num < mn:
            mn = num

    print("#{} {}".format(tc, mx-mn))