import sys

sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maps = list(map(int,input().split()))
    mx = mx_idx = 0
    buy_money = get_money = 0
    position = 0
    while True:
        if mx_idx == n-1: # 위치가 마지막에 도달하면 종료
            break
        buy_money = 0
        mx = 0
        for i in range(position, n): # 위치부터 최댓값 구하기
            if maps[i] > mx:
                mx = maps[i]
                mx_idx = i

        for i in range(position, mx_idx): # 위치부터 최대값 전까지 매수
            buy_money += maps[i]

        if buy_money != 0:
            get_money += mx*(mx_idx-position) - buy_money # 매수했던거 최대값에 매도
        position = mx_idx+1 # 최대값 이후부터 다시 시작


    print("#{} {}".format(tc, get_money))