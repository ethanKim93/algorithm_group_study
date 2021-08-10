import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    Info = list(map(int, input().split()))  # K,M,N 정보 (이동, 정류장수, 충전기)
    N_location = list(map(int, input().split())) # 충전기 설치장 위치
    K, N, M = Info[0], Info[1], Info[2]

    bus_stay = [0] * (N+1)
    for i in range(len(N_location)): # 카운트 정렬활용
        bus_stay[N_location[i]] += 1
    start = 0
    end = K
    charge = 0

    while 1: # 무한루프
        no_charge = 0
        for idx in range(start+1, end+1): # k만큼 이동
            if bus_stay[idx] == 1:
                start = idx
            else:
                no_charge += 1
        if no_charge == K: # 충전소가 없는지 확인
            charge = 0
            break
        charge += 1
        end = start + K

        if end >= N:
            break

    print('#{} {}'.format(tc, charge))







