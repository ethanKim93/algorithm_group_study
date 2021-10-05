import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    schedule = []
    for _ in range(N):
        s, e = map(int, input().split())
        schedule.append((s,e))

    # 종료 시간이 빠르되 시작시간이 늦은 순으로 정렬
    # schedule.sort(key=lambda x: (x[1], -x[0]))
    schedule.sort(key=lambda x: x[1])
    cnt = i = current = 0
    while i<N:
        # 현재 시간보다 시작 시간이 같거나 뒤에 있을 때 작업 가능
        if current <= schedule[i][0]:
            # 작업의 종료시간으로 현재 시간 갱신
            current = schedule[i][1]
            cnt += 1
        # 다음 작업 확인
        i += 1
    print('#{} {}'.format(tc, cnt))

