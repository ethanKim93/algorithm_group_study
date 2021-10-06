import sys
sys.stdin = open("input.txt")
#5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]
    times.sort(key=lambda x: (x[1])) # 걍 sort하면 시작 값을 기준으로 정렬되므로
    end = times[0][1]
    cnt = 1
    for i in range(1, N):
        if times[i][0] >= end:
            end = times[i][1]
            cnt += 1
    print('#{} {}'.format(tc, cnt))