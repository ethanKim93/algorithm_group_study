import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    K,N,M = map(int, input().split())
    stop = list(map(int, input().split()))

    now = 0
    cnt = 0

    while now < N:
        now += K
        if now >= N:
            break
        for i in range(now, now-K, -1):
            if i in stop:
                now = i
                cnt += 1
                break
        else:
            cnt = 0
            break

    print('#{} {}'.format(tc, cnt))