import sys
sys.stdin = open('input.txt')

T = int(input())  # 노선 수
for tc in range(1, T+1):
    k, n, m = map(int, input().split())
    # k:한번충전가동, n:종점, m:충전설치장소
    charge_list = list(map(int, input().split())) + [n+k, n+k]
    # 충전기 위치
    # n+k를 2개 추가해주는 이유는 밑에 while문에서 마지막 값이 범위를 벗어나기 때문에 만들어준것이다.

    st = 0
    #현재 위치
    i = 0
    #정류장 위치
    cnt = 0
    #충전할 때마다 +1

    while st + k < n:
    # 현재위치에서 최대 이동가능한 만큼 이동했을때 종점보다 작을때 동안만 반복.
        if st + k >= charge_list[i+2]:
        #만약 현재위치에서 최대 이동가능한 만큼 이동한 것이 충전소의 위치의 +2보다 크다면
            st = charge_list[i+2]
            #현재 위치가 그 충전소의 위치가 된다.
            cnt += 1
            #충전 1회 추가.
            i += 3
            #정류장 위치를 3만큼 더함.
            continue

        elif st + k >= charge_list[i+1]:
        # 만약 현재위치에서 최대 이동가능한 만큼 이동한 것이 충전소의 위치의 +1보다 크다면
            st = charge_list[i+1]
            #현재 위치가 그 충전소의 위치가 된다.
            cnt += 1
            #충전 1회 추가.
            i += 2
            #정류장 위치를 2만큼 더함.
            continue

        elif st + k < charge_list[i]:
        # 또한 만약에 현재위치에서 최대 이동가능한 만큼 이동한 것이 충전소 위치보다 작으면
            cnt = 0
            #충전 불가. cnt = 0
            break
            #더이상 움직일 수 없으니 break

        else:
            st = charge_list[i]
            #나머지 경우는 현재 위치와 충전 위치를 같게 해주고
            cnt += 1
            # 충전 1회 추가.
            i += 1
            # 정류장 위치를 1만큼 더함.

    print('#{} {}'.format(tc, cnt))

