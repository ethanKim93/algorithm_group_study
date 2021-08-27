import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    loc = [i for i in range(1, 1 + N)]
    oven = []
    cnt = 0
    for _ in range(N):
        cnt += 1
        oven.append(pizza.pop(0))

    while len(loc) > 1:
        oven[0] //= 2
        if oven[0]:
            oven.append(oven.pop(0))
            loc.append(loc.pop(0))
        else:
            if pizza:
                cnt += 1
                oven[0] = pizza.pop(0)
                loc[0] = cnt
                oven.append(oven.pop(0))
                loc.append(loc.pop(0))
            else:
                oven.pop(0)
                loc.pop(0)

    print("#{} {}".format(tc, loc[0]))