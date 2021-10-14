# 라이브 설명대로 풀었다

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    ans = []

    for money in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
        div = N // money
        N = N % money
        ans.append(div)

    print('#{}'.format(tc))
    print(*ans)
