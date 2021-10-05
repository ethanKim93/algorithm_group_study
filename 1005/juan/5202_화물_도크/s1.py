import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    # N개
    N = int(input())
    # 시작과 종료 시간
    jobs = [list(map(int, input().split())) for _ in range(N)]

    # 종료 시간 순으로 정렬
    jobs.sort(key=lambda x : x[1])
    # print(jobs)

    ans = 1
    finish_time = jobs[0][1] # 0번 작업의 종료 시간을 임의로 잡고 시작

    for i in range(1, N):
        # 0번 이후부터 시작 시간을 종료 시간과 비교해서 크거나 같은 경우
        # (종료 시간이 5시면 다음 작업 시간은 5시부터 가능하니 '이상'으로 처리)
        if jobs[i][0] >= finish_time:
            # 최대 화물차 숫자 1 누적
            ans += 1
            # 시작 시간을 종료 시간으로 변경
            finish_time = jobs[i][1]
    print('#{} {}'.format(tc, ans))