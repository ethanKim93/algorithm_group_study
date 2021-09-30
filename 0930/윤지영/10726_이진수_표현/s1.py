import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    ans = 'ON'
    for i in range(N):
        if (1<<i) & M == 0:
            ans = 'OFF'
            break
    print('#{} {}'.format(tc, ans))
