import sys

sys.stdin = open('sample_input.txt')


def function(cnt):
    # 가장 적게 이용하는 화물을 찾을 변수
    min_time = 25
    tmp = 0
    for i in range(N):
        # 작업에 포함된 화물은 pass
        if switch[i]:
            continue
        s, e = start_end[i]
        # 해당 화물이 차지하는 작업 시간이
        # 이미 다른 화물에 할당되어 있으면 break
        # 즉, 해당 화물은 작업 가능하지 않다면 break
        for t in range(s, e):
            if time[t] == 1:
                break
        # 해당 화물이 작업 가능하다면
        else:
            # 남은 화물 중에서 해당 화물이 가장 적게 이용하는 경우라면 갱신
            less_time = e - s
            if min_time > less_time:
                min_time = less_time
                tmp = i
    # 값이 갱신되지 않았다면, 더이상 작업할 수 있는 화물이 없다는 뜻
    if min_time == 25:
        return cnt

    # 값이 갱신되었다면, 해당 화물을 체크하고, 시간을 할당한다.
    switch[tmp] = 1
    start, end = start_end[tmp]
    for t in range(start, end):
        time[t] = 1
    # 재귀 (남은 화물 가지고 다시 조사)
    return function(cnt + 1)


T = int(input())

for tc in range(T):
    N = int(input())
    # [시작시간, 종료시간]
    start_end = [list(map(int, input().split())) for _ in range(N)]

    time = [0] * 24    # 0시 ~ 24시
    switch = [0] * N   # 작업 가능한 화물 체크

    print('#{} {}'.format(tc + 1, function(0)))