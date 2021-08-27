import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    cheese = [0] + list(map(int, input().split()))
    pizzas = [i for i in range(1, len(cheese))]
    oven = []

    for _ in range(N):
        p = pizzas.pop(0)
        oven.append(p)

    while True:
        if len(oven) == 1:
            break
        front = oven.pop(0)
        cheese[front] //= 2

        if cheese[front] == 0:
            if pizzas:
                oven.append(pizzas.pop(0))
        else:
            oven.append(front)

    print('#{} {}'.format(tc,oven[0]))



