
import sys
sys.stdin = open('input.txt')
T = int(input())


# 현종일 (최종)
def charge(now, cnt):
    global result
    battery = charge_area[now]

    if cnt > result:
        return

    if now+battery >= N:
        if cnt <= result:
            result = cnt
        return

    for i in range(1, battery+1):
        if now+i < N:
            charge(now+i, cnt+1)

for tc in range(1, int(input())+1):
    charge_area = list(map(int,input().split()))
    N = charge_area[0] # 1번 인덱스부터 쓰기 위해 pop을 쓰지 않음
    result = 100

    charge(1, 0)
    print('#{} {}'.format(tc, result))