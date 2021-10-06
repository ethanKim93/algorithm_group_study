import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]
    times.sort(key=lambda x : (x[1], x[0]))
    starttime = 0
    cnt = 0
    for idx in range(len(times)):
        if starttime <= times[idx][0]:
            cnt += 1
            starttime = times[idx][1]
    print('#{} {}'.format(tc, cnt))