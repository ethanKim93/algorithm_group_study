import sys
sys.stdin=open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    profit = 0
    max_price = 0
    for i in range(N-1, -1, -1):
        if max_price < prices[i]:
            max_price = prices[i]
        else:
            profit += max_price - prices[i]
    print('#{} {}'.format(tc, profit))