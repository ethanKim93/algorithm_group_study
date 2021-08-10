import sys
sys.stdin=open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charges = list(map(int, input().split())) + [N]     #

    cnt = 0     # 충전 횟수
    bus = 0     # 버스의 위치

    for i in range(M+1):
        if bus + K >= N:                        # 버스가 종착역을 지나면 반복문 종료
            break
        elif bus + K < charges[i]:              # 버스 위치 + 최대 이동 거리 < i번째 충전소이고
            if charges[i-1] + K >= charges[i]:  # 직전 충전소 위치 + 최대 이동 거리 >= i번째 충전소 위치라면
                cnt += 1                        # 충전 횟수 += 1
                bus = charges[i-1]              # 버스 위치를 직전 충전소 위치로 이동
            else:                               # i-1 충전소와 i번째 충전소의 거리가 최대 이동 거리보다 크면 cnt=0
                cnt = 0
                break
        else:
            pass

    print('#{} {}'.format(tc, cnt))