import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(0, T):
    N = int(input())
    a = b = c = d = e = 0
    while N >= 1:
        if N%2 == 0:
            N = N/2
            a += 1
        elif N%3 == 0:
            N = N/3
            b += 1
        elif N%5 == 0:
            N = N/5
            c += 1
        elif N%7 == 0:
            N = N/7
            d += 1
        elif N%11 == 0:
            N = N/11
            e += 1
        else:
            break
    print("#{} {} {} {} {} {}".format(i+1, a, b, c, d, e))