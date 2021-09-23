import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    # 예약한 손님을 오름차순(시간순)으로 정렬한다.
    reservation = sorted(list(map(int, input().split())))

    time = 0
    bread = 0
    reserve_idx = 0
    result = True

    while reserve_idx < N:
        # 시간에 따라 빵을 구워낸다.
        if time and not time % M:
            bread += K

        # 예약손님이 되면 빵을 주고 손님을 내보낸다.
        while reserve_idx < N and reservation[reserve_idx] == time:
            reserve_idx += 1
            bread -= 1

        # 빵이 0보다 작은 경우라면 불가능한 경우이므로 result = False로 둔다.
        if bread < 0:
            result = False
            break
        time += 1

    result = "Possible" if result else "Impossible"
    print("#{} {}".format(tc, result))

