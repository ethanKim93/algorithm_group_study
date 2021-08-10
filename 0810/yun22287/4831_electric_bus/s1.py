import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split())) + [N]
    a = 0
    cnt = 0
    n = K+1
    while a <= N:
        n -= 1
        if a == N :
            cnt -= 1
            break
        elif a + n in station:
            cnt += 1
            a += n
            n = K+1
        elif a + K < station[cnt]:
            cnt = 0
            break
    print('#{0} {1}'.format(tc, cnt))