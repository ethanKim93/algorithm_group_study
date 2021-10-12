import sys
sys.stdin = open('input.txt')

T = int(input())
coin = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for test_case in range(1,T+1):
    money = int(input())
    coins=[0]*8
    for i in range(len(coin)):
        coins[i] = money//coin[i]
        money %= coin[i]
    print('#{}'.format(test_case))
    print(*coins)