import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    cards = list(map(int, input()))
    temps = [0] * 10
    # 가장 많은 카드의 숫자: mx, 가장 많은 카드의 장 수: mx_num
    mx = mx_num = 0

    for card in cards:
        temps[card] += 1

    for i in range(10):
        if temps[i] >= mx_num:
            mx_num = temps[i]
            mx = i

    print("#{} {} {}".format(tc, mx, mx_num))