import sys
sys.stdin = open('sample_input.txt')


def total_price(product, price):
    global minV
    if price >= minV:
        return

    if product == N:
        minV = price
        return

    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            total_price(product+1, price+cost[product][i])
            visit[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    minV = 987654321
    visit = [0] * N
    total_price(0, 0)

    print('#{} {}'.format(tc, minV))