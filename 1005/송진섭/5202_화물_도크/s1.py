import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time_table = [list(map(int, input().split())) for _ in range(N)]
    time_table.sort(key=lambda x: (x[1], x[0]))
    print(time_table)
    time_table.sort(key=lambda x: (x[1], -x[0]))
    print(time_table)
    # 시간표를 작업 끝나는 시간, 시작 시간에 맞쳐 정렬
    cnt = 1
    end_time = time_table[0][1]
    # 처음 활동 카운트, 끝나는 시간 지정
    for i in range(1, len(time_table)):
        # 처음 제외하고 1부터 비교
        if end_time > time_table[i][0]:
            # 끝 시간이 다음 시작시간 보다 크면 무시
            continue
        cnt += 1
        end_time = time_table[i][1]
        # if문에 안들어가고 활동이 카운트되면 끝 시간 갱신신
    print('#{} {}'.format(tc, cnt))
