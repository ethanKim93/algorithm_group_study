import sys
sys.stdin = open('sample_input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    cnt = 0
    times = []                #
    end = 0
    for _ in range(N):
        s,e = map(int, input().split())
        times.append([s,e])
    times.sort(key=lambda x: (x[1], x[0]))   # 각 튜플의 종료시간,시작시간 순으로 오름차순정렬

    for time in times:
        if time[0] >= end:
            cnt += 1
            end = time[1]
    print('#{} {}'.format(tc, cnt))