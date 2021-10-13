import sys

sys.stdin = open('input.txt')
T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]


for tc in range(1, T + 1):
    cnt = [0] * 8
    N = int(input())
    for i in range(len(money)):
        if money[i] > N:
            continue
        else:
            while money[i] <= N:
                N=N-money[i]
                cnt[i]+=1

    print('#{}'.format(tc))
    for i in range(len(cnt)):
        print(cnt[i],end=' ')
    print()