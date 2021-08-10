import  sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    number = int(input())
    a = b = c = d = e = 0
    while number != 1:
        if not number % 2:
            number //= 2
            a += 1
        elif not number % 3:
            number //= 3
            b += 1
        elif not number % 5:
            number //= 5
            c += 1
        elif not number % 7:
            number //= 7
            d += 1
        elif not number % 11:
            number //= 11
            e += 1
    print('#{} {} {} {} {} {}'.format(tc, a, b, c, d, e))