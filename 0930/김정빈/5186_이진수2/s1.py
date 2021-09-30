#5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2
T = int(input())
for tc in range(1, T+1):
    n10 = float(input())
    ns = ""
    calc = n10 * 2
    while len(ns) < 13 and calc != 1.0:
        if calc >= 1.0:
            calc -= 1.0
            ns += "1"
        else:
            ns += "0"
        calc *= 2

    if len(ns) >= 13:
        print('#{} {}'.format(tc, 'overflow'))
    else:
        print('#{} {}'.format(tc, ns+"1"))