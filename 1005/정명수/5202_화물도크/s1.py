import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    time = []
    for _ in range(N):
        i,j = map(int,input().split())
        time.append((i,j))
    time.sort(key = lambda x:(x[1],x[0]))

    cnt = 1
    end_time = time[0][1]
    for k in range(1,N):
        if time[k][0] >= end_time:
            cnt += 1
            end_time = time[k][1]

    print('#{} {}'.format(tc,cnt))