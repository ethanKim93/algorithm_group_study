import sys
sys.stdin=open('input.txt')
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    time = []
    for i in range(N):
        time.append(list(map(int, input().split())))

    time = sorted(time, key=lambda x: x[1])
    print(time)
    cnt = 0
    cactime = 0
    for i in range(N):
        start = time[i][0]
        end = time[i][1]

        if cactime <= start:
            cnt += 1
            cactime = end

    print('#{} {}'.format(tc, cnt))
