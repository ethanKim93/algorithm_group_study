import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maps = [50000,10000,5000,1000,500,100,50,10]
    ans = []
    while maps:
        cnt = 0
        money = maps.pop(0)
        while n >= money:
            n -= money
            cnt += 1

        ans.append(cnt)

    print("#" + str(tc))
    print(*ans)
# Pass