import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    numbers = [i for i in range(1,13)] # 1~12 list
    n, k = map(int, input().split())
    ans = 0

    # Bitmask for subset
    for i in range(1<<12):
        temps = [] # Subset
        cnt = sm = 0

        for x in range(12):
            if i & (1<<x):
                temps.append(numbers[x])

        # =len(temps)
        for y in temps:
            cnt += 1

        # =sum(temps)
        if cnt == n:
            for z in temps:
                sm += z

        if sm == k:
            ans += 1

    print("#{} {}".format(tc, ans))