import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))

    total = 0

    max_price = price[-1]

    for i in range(N - 2, -1, -1):
        if max_price > price[i]:
            total += max_price - price[i]
        else:
            max_price = price[i]

    print('#{} {}'.format(tc, total))