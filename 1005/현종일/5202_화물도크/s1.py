import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):
    N = int(input())
    requirements = [list(map(int, input().split())) for _ in range(N)]

    # 받아온 신청서를 1순위로 종료시간, 2순위로 시작시간 기준으로 오름차순
    requirements.sort(key=lambda x: (x[1], x[0]))

    cnt = 0                     # 총 작업 갯수 카운팅
    end = 0                     # 현재 종료 시간
    for req in requirements:
        if req[0] >= end:       # 시작 가능한 작업이라면
            cnt += 1            # 작업 갯수 +1
            end = req[1]        # 현재 종료 시간 재정의

    print("#{} {}".format(tc, cnt))