import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    price = list(map(int, input().split()))
    max_price = price[-1]
    ans = 0

    for i in range(N-2, -1, -1):
        if max_price > price[i]:
            ans += max_price - price[i]
        else:
            max_price = price[i]

    print('#{} {}'.format(tc, ans))