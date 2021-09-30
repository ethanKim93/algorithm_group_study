import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    std = (2**N)-1
    if std == (M & std):
        ans = 'ON'
    else: ans = 'OFF'
    print('#{} {}'.format(tc,ans))