import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # N은 도크 사용 신청서 개수
    time_list = []
    for _ in range(N):
        s, e = map(int, input().split())
        # s는 시작 시간, e는 종료 시간
        time_list.append([s, e])

    sorted_time = sorted(time_list, key=lambda x: x[1])
    # 종료 시간 기준 정렬

    cnt = 0
    time = 0
    # 종료시간
    for i in range(N):
        start = sorted_time[i][0]
        end = sorted_time[i][1]

        if time <= start:
            cnt += 1
            time = end

    print('#{} {}'.format(tc, cnt))
