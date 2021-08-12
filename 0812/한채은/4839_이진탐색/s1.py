import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    cnt_A = 0
    cnt_B = 0
    L = 1
    R = P

    # A 찾기
    while True:
        c = int((L+R)/2)
        cnt_A += 1
        if c == Pa:
            break
        elif c <= Pa:
            L = c
        else:
            R = c
    L = 1
    R = P

    # B 찾기
    while True:
        c = int((L+R)/2)
        cnt_B += 1
        if c == Pb:
            break
        elif c <= Pb:
            L = c
        else:
            R = c

    if cnt_A > cnt_B:
        print('{} {}'.format(tc, 'B'))
    elif cnt_A < cnt_B:
        print('{} {}'.format(tc, 'A'))
    else:
        print('{} {}'.format(tc, 0))



