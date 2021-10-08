# fail
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    bus_stop = list(map(int, input().split()))
    destination = bus_stop[0]
    bus_stop = bus_stop + [0]
    battery = bus_stop[1]
    now = 1
    cnt = 0
    while now != destination:
        now += 1
        battery -= 1
        if battery >= destination - now:
            continue
        if bus_stop[now] >= destination - now or not battery:
            battery = bus_stop[now]
            cnt += 1
    print('#{} {}'.format(tc, cnt))

