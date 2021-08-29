import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ci = list(map(int, input().split()))
    pizza = []
    for index, val in enumerate(ci):
        pizza.append([index+1, val])
    oven = [0] * N
    for i in range(N):
        oven[i] = pizza.pop(0)
    while oven != [0] * N:
        for j in range(len(oven)):
            if oven[j] != 0:
                if oven[j][1] // 2:
                    oven[j][1] //= 2
                    idx = oven[j]
                else:
                    if pizza:
                        oven[j] = pizza.pop(0)
                    else:
                        oven[j] = 0
    print('#{} {}'.format(tc, idx[0]))
