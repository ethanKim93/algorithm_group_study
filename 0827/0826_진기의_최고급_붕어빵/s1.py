import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    t = list(map(int, input().split()))
    time_end = 0
    time_a = 0
    time_b = 0
    bread = 0
    cus = len(t)
    while cus >= 1:
        time_a += 1
        time_b += 1
        for i in range(len(t)):
            if time_b == t[i]:
                bread -= 1
        if bread < 0:
            cus = 1
            break
        if time_a == M:
            bread += K
            time_a = 0
        cus -= 1
    if bread >= 0:
        print('#{} {}'.format(tc + 1, 'Possible'))
    elif bread < 0:
        print('#{} {}'.format(tc + 1, 'Impossible'))
