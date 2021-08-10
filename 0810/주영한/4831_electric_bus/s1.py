import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    # K : 최대 이동 가능한 정류장 수, N : 종점인 정류장, M = 충전기 갯수
    K, N, M = map(int, input().split())

    # 충전기에 대한 정보를 path에 저장한다. 시작점 또한 추가하기 위해 N+1을 사용하였다.
    path = [0] * (N + 1)

    # 정류장 위치에 대한 충전기 여부를 확인한다 (1 : 있음 / 0 : 없음)
    stations = map(int, input().split())
    for station in stations:
        path[station] = 1

    # 충전 횟수를 나타내는 charge_time 와 현재 위치를 나타내는 location
    charge_time = 0
    location = 0

    # location + K일 경우, 현재 위치에서 이동할 수 있는 거리이므로 이가 N보다 작을 경우 반복한다.
    while location + K < N:
        # 도착이 불가능 한 경우를 나타내는 impossible 변수 선언한다.
        impossible = True

        # move의 경우 K, K-1, ..., 2, 1로 주어진다.
        # 가장 멀리 이동한 경우부터 확인한다.
        for move in range(K, 0, - 1):
            if path[location + move] == 1:
                # 움직일 수 있는 거리 중 가장 멀리 떨어진 충전소를 확인하면
                # 위치 및 충전 횟수를 최신화 한다.
                impossible = False
                charge_time += 1
                location = location + move
                break
        if impossible:
            # 불가능한 경우 charge_time = 0으로 하고 while 문을 빠져 나옴
            charge_time = 0
            break

    print("#{} {}".format(tc, charge_time))