import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())

    # 충전기에 대한 정보를 path에 저장함
    path = [0] * (N + 1)
    stations = map(int, input().split())
    for station in stations:
        path[station] = 1

    if

    charge_time = 0     # 충전 횟수를 나타내는 charge_time
    location = 0        # 현재 위치를 나타내는 location

    while location + K < N:
        # location + K일 경우, 현재 위치에서 이동할 수 있는 거리
        impossible = True
        # 도착이 불가능 한 경우를 나타내는 impossible 변수 선언
        for move in range(K, 0, - 1):
            if path[location + move] == 1:
                # 움직일 수 있는 거리 중 가장 멀리 떨어진 충전소를 확인
                impossible = False
                charge_time += 1
                location = location + move
                #충전하고 해당 위치로 이동
                break
        if impossible:
            # 불가능할 경우 charge_time = 0으로 하고 while 문을 빠져 나옴
            charge_time = 0
            break

    print("#{} {}".format(tc, charge_time))