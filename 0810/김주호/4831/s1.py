import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for case in range(T):
    K, N, M = map(int, input().split()) # 최대 이동 거리, 정류장 개수, 충전기 대수
    charge_stations = list(map(int, input().split())) # 충전기 설치 정류장

    i = 0 # 충전기 설치 정류장 col
    cnt = 0 # 충전 횟수
    station = 0 # 현재 위치
    end = False # 마지막 정류장 도달 유무

    while station < N + 1: # 현재 버스가 마지막 정류장에 도달하지 못 하여 운행중일 때
        far_charge_station = 0 # 가장 먼 충전기 설치 정류장
        for max_move in range(1, K + 1): # 버스의 최대 이동 거리로 for문 돌리기
            if station + max_move == N: # 만약 현재 위치 + 버스 이동거리로 마지막 정류장 도달 가능하다면
                end = True # 끝내기 모드 활성화
                break
            elif i != M and station + max_move == charge_stations[i]: # 이동거리 기준 가장 먼 충전기 정류장울 찾음
                far_charge_station = charge_stations[i]
                i += 1 # 목표를 다음 충전기 정류장으로, 만약 이미 마지막 충전기 정류장이었다면 elif가 돌지 않게끔

        if end: # 끝내기 가능?
            break

        elif far_charge_station: # 가장 먼 충전기 정류장을 찾았다면
            station = far_charge_station # 그곳으로 이동하여 충전
            cnt += 1 # 충전 횟수 증가

        else: # 충전 불가라면
            cnt = 0 #강종
            break



    print("#{} {}".format(case + 1, cnt))
