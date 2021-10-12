import sys
sys.stdin = open('input.txt')

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    print('#{}'.format(tc))
    while cnt < 8:
        print(N // money[cnt], end=' ')
        N %= money[cnt]
        cnt += 1
    print()