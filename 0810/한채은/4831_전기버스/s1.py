import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    # K: 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # N: 종점
    # M: 충전기가 설치된 정류장 수
    K, N, M = map(int, input().split())

    # 충전기의 위치
    electric_station = list(map(int, input().split()))

    # 충전기 위치를 표시함
    bus_stop = [0] * (N+1)

    # 충전기가 있으면 1 없으면 0
    for i in electric_station:
        bus_stop[i] += 1

    cnt = 0
    bus = 0

    while True:
        bus += K

        if bus >= N:
            break
        # 만약 bus의 위치를 넣어주었을 때
        for j in range(bus, bus-K, -1):
            # 1이 있다면 cnt 1개 올리고 for문을 빠져나와서
        # while문 바로 아래의 bus += K로 돌아감
            if bus_stop[j]:
                cnt += 1
                bus = j
                break

        else:
            cnt = 0
            break

    print('#{} {}'.format(tc, cnt))