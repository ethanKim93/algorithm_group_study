import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):
    #N 번 정류장까지, 최대 이동정류장 수 = K, 충전기 설치된 M개의 정류장 번호
    K, N, M = map(int, input().split())
    charge_list = list(map(int, input().split()))

    bus = cnt = 0
    while( bus < N ):
        bus += K
        if bus >= N:
            break

        if bus in charge_list:
            cnt += 1
        else:
            for pos in range(bus-1,bus-K,-1):
                if pos in charge_list:
                    bus = pos
                    cnt += 1
                    break
            else:
                cnt = 0
                break

    print('#{} {}'.format(tc, cnt))