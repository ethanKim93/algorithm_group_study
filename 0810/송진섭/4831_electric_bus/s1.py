import  sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split()) #K:최대이동거리 N:목적지까지 거리 M:충전기 설치 정류장 수
    M_list = list(map(int, input().split())) # 충전기 정류장 번호
    # print(M_list)
    distance = [0] * (N+1) #전체구간 만들기
    for i in range(len(distance)): # 충전소 구간에 +1
        for j in range(len(M_list)):
            if i == M_list[j]:
                distance[i] += 1

    cnt = 0 #충전횟수
    bus = K # 버스충전량
    bus_i = 0 #버스위치
    bus_muhan = 0

    while bus_i < N:
        if bus == 0 and distance[bus_i] == 1:  # 충전이 필요하고 충전소가 있는 경우 충전
            bus += K
            cnt += 1
        elif bus == 0 and distance[bus_i] == 0:  # 충전이 필요하고 충전소가 없는 경우 뒤로가기
            bus_i -= 1
            bus_muhan += 1
            if bus_muhan >= K:  # 뒤로가기를 최대로 가는경우 목적지 못가고 무한루프
                cnt = 0
                break
        else:  # 정상적으로 가는 경우
            bus_i += 1
            bus -= 1
            bus_muhan = 0
    print(cnt)