import sys
sys.stdin = open('input.txt')

for case in range(int(input())):
    N = int(input())
    plan = [list(map(int, input().split())) for _ in range(N)]
    plan.sort(key=lambda p: p[1])       # 2차원 배열끝나는 시간 순 정렬
    total = 0                           # 배정 횟수
    time = 0                            # 끝나는 시간 담을 변수
    for s, e in plan:                   # 0시 시작
        if time <= s:                   # 정렬된 리스트에서 현재 시간이 리스트의 시작시간보다 작거나 같을경우
            total += 1                  # 배정 횟수 +1
            time = e                    # 현재시간을 끝나는 시간으로 변경

    print("#{} {}".format(case + 1, total))
    # ans = 0
    # N = int(input())
    # time_table = [list(map(int, input().split())) for _ in range(N)]
    # time_table.sort(key=lambda x:x[0])
    # # print(time_table)
    #
    # for i in range(len(time_table)):
    #     time_table[i].append(time_table[i][1]-time_table[i][0])
    # use = 0
    # capa = [0]*25
    # for i in range(len(time_table)):
    #     try:
    #         if time_table[i][0] == time_table[i+1][0]:
    #             if time_table[i][2] > time_table[i+1][2]:
    #                 use = time_table[i+1][2]
    #
    #     except:
    #         pass
    #
    #
    # print(time_table)
    #
    # print('#{} {}'.format(tc, ans))