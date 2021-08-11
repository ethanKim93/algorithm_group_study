import sys

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    counts = [0] * (N+1)    # 0번 정류장부터 N번 정류장까지 초기화
    chargers = list(map(int, input().split()))
    cnt = 0
    end_station_flag = 1

    for charger in chargers:
        counts[charger] += 1

    for i in range(M-1):        # 충전기 설치 정류장 사이 간격이 최대 거리보다 크면 아래 반복문을 돌지 않고 0 출력
        if chargers[i+1] - chargers[i] > K:
            end_station_flag = 0

    i = 0
    while end_station_flag:
        if i+K >= N:        # 충전 안하고 갈수있는 최대거리 내에 종착역이 있으면 종료
            break

        for j in range(i+K, i, -1):     # 갈수있는 최대거리부터 1씩 인덱스를 낮추면서 충전기가 있는 정류장 확인 및 횟수 카운트
            if counts[j]:
                i = j
                cnt += 1
                break

    print('#{} {}'.format(tc, cnt))
