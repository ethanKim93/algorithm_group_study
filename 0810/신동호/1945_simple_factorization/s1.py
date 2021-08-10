import sys
sys.stdin = open('input.txt')

T = int(input())
#짧게 할 수 있겠지만 오랜만에 옛날 감성으로 일부러 길게 해봤습니다
for tc in range(1, T+1):
    num = int(input())
    a = b = c = d = e = 0
    while not num%2:
        a += 1
        num /= 2
    while not num%3:
        b += 1
        num /= 3
    while not num%5:
        c += 1
        num /= 5
    while not num%7:
        d += 1
        num /= 7
    while not num%11:
        e += 1
        num /= 11
    print('#{} {} {} {} {} {}'.format(tc, a, b, c, d, e))