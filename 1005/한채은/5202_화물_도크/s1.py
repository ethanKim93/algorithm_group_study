import sys
sys.stdin = open('sample_input.txt')

for case in range(int(input())):
    N = int(input())
    plan = [list(map(int, input().split())) for _ in range(N)]

    # plan[idx][0]이 시작시간 plan[idx][1]이 종료시간
    # sort에 내장되어있는 key를 이용해 종료시간 기준으로 정렬
    # 그러면 시간순으로 sort 가능
    plan.sort(key=lambda p: p[1])

    # 몇개의 화물차가 이용할 수 있는지 담는 변수 total
    total = 0
    time = 0
    # plan에 있는 start와 end 돌면서
    for s, e in plan:
        # 만약에 time이 s보다 작으면
        if time <= s:
            # total에 하나 올려주고
            total += 1
            # time을 end로 update
            time = e

    print("#{} {}".format(case + 1, total))