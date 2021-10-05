import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    time = []

    # 시작 시간과 종료 시간
    for n in range(N):
        time.append(tuple(map(int,input().split())))

    # 종료 시간이 빠른 순서대로 정렬하기
    time.sort(key=lambda element : element[1])

    cnt = 1
    start, end = time[0]
    for i in range(N):
        # i번째의 시작 시간이 전 작업의 종료 시간 이후라면
        if time[i][0] >= end:
            cnt += 1
            start, end = time[i]

    print('#{} {}'.format(tc, cnt))