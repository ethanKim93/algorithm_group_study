import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    timeline = [list(map(int, input().split())) for _ in range(N)]

    timeline.sort(key=lambda x: (x[1], x[0]))
    end_time = timeline[0][1]
    cnt = 1

    for i in range(1, len(timeline)):
        if timeline[i][0] >= end_time:
            cnt += 1
            end_time = timeline[i][1]
    print('#{} {}'.format(tc, cnt))