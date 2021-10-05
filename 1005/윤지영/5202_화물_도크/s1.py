import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    time_list = [list(map(int,input().split())) for _ in range(N)]
    time = sorted(time_list, key=lambda x :x[1])
    i = cnt = 0
    for s,e in time:
        if s >= i:
            cnt += 1
            i = e
    print('#{} {}'.format(tc,cnt))
