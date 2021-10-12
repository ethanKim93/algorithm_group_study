import sys
sys.stdin = open('input.txt')

money = [50000,10000,5000,1000,500,100,50,10]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    result = []
    for i in range(8):
        cnt = 0
        while money[i] <= N:
            cnt += N//money[i]
            N %= money[i]
        result.append(cnt)
    print('#{}'.format(tc))
    print(' '.join(map(str,result)))

