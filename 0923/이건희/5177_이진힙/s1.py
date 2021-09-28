import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maps = [0] + list(map(int,input().split()))
    for i in range(2, n+1):
        next = i // 2
        while next != 0:
            if maps[i//2] > maps[i]:
                maps[i//2], maps[i] = maps[i], maps[i//2]
                next = next // 2
                i = i//2
            else:
                break

    ans = 0
    while n//2 != 0:
        ans += maps[n//2]
        n //= 2

    print("#{} {}".format(tc, ans))