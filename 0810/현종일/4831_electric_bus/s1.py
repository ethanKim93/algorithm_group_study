import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    case = list(map(int, input().split()))
    stop_no = list(map(int, input().split()))

    # 전체 정류장 배열에 충전기가 있을시 1을 대입
    stop = [0] * case[1]
    for i in stop_no:
        stop[i] = 1

    # 버스위치 초기화, cnt 초기화
    bus = 0
    cnt = 0

    # 종점 정류장에 도착하면 while문 종료
    while bus + case[0] < case[1]:
        # 끝부터 순회
        for j in range(case[0], -1, -1):
            # 충전기가 없다면
            if j == 0:
                cnt = 0
                # 최대 정류장 번호인 100을 더해 종료
                bus += 100
            elif stop[bus + j] == 1:
                bus += j
                cnt += 1
                break
    print('#{} {}'.format(tc, cnt))



