import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    route = list(map(int,input().split()))
    K,N,M = route[0], route[1], route[2]
    station = list(map(int, input().split()))
    station.append(N)
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
            continue
        elif a + K < station[cnt] :
            cnt = 0
            break
    print('#{0} {1}'.format(tc, cnt))