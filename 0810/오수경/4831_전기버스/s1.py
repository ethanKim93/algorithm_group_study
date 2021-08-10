import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    k, N, M = map(int, input().split())
    bus_stop = list(map(int, input().split()))



    bus = 0
    cnt = 0

    # error 인 경우
    interval_list = []
    for m in range(M-1):
        interval = abs(bus_stop[m]-bus_stop[m+1])
        interval_list.append(interval)

    for i in interval_list:
        if i > k:
            print('#{} {}'.format(tc, 0))
            break


    else:
        while bus < N:
            bus += k
            if bus >= N:
                break
            elif bus not in bus_stop and bus <= N:

                while bus not in bus_stop:
                    bus -= 1
                cnt += 1

            else:
                if bus > N:
                    break
                cnt += 1

        print('#{} {}'.format(tc, cnt))

