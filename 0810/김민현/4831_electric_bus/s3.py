T = int(input())

for test_case in range(1, T + 1):
    cnt = 0
    k, n, m = map(int, input().split())  # k:한번충전가동, n:종점, m:충전설치장소
    chrg = list(map(int, input().split()))

    rmn = k
    point = 0
    for i in range(len(chrg)):
        if i == len(chrg) - 1:  # 마지막 위치이면
            if n - point > rmn: #종점에서 현재 위치와의 거리가 k 보다 작을 경우
                cnt += 1

        elif chrg[i] - point <= rmn: #충전소 =현재 위치의 차이가
            if chrg[i + 1] - point > rmn:
                rmn = k
                cnt += 1
            else:
                rmn -= (chrg[i] - point)
            point = chrg[i]
        else:  # 종점에 도착못할 경우
            cnt = 0
            break

    print("#" + str(test_case), cnt)