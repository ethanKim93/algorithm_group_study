import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    cost = prices[-1]
    result = 0
    for price in prices[::-1]:
        if price < cost:
            result += cost-price
        else:
            cost = price
    print('#{} {}'.format(tc,result))