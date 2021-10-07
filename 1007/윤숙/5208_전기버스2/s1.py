# 런타임 에러
import sys
sys.stdin = open('input.txt')
T = int(input())

#런타임 에러
def cac_mincharge(now, cnt):
    global charge
    if cnt > charge:

        return

    if now >= busstop_n - 1:
        if charge >= cnt:
            charge = cnt

        return
    else:

        for i in range(battery[now]):
            if now + i + 1 < busstop_n:
                cac_mincharge(now + i + 1, cnt + 1)


for tc in range(1, T + 1):
    # 한 줄에 정류장 수 N, N-1개의 정류장 별 배터리 용량 Mi

    arr = list(map(int, input().split()))
    busstop_n = arr[0]
    battery = arr[1:]

    charge = 100
    cac_mincharge(0, -1)
    print('#{} {}'.format(tc, charge))
