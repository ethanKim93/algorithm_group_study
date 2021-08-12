# start = middle, end = middle로 해야 답 나옴
# 성공여부를 담는 변수를 만들어서 못찾았으면 True를 반환하게 했는데 굳이 필요 없는듯함

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    # A 탐색
    l = 1
    r = P
    cnt_A = 0
    A_fail = False
    while l <= r:
        cnt_A += 1
        c = (l + r) // 2
        if c == Pa:
            break
        elif c > Pa:
            r = c
        else:
            l = c
    if c != Pa:
        A_fail = True

    l = 1
    r = P
    cnt_B = 0
    B_fail = False
    # B 탐색
    while l <= r:
        cnt_B += 1
        c = (l + r) // 2
        if c == Pb:
            break
        elif c > Pb:
            r = c
        else:
            l = c
    if c != Pb:
        B_fail = True

    winner = ''
    if A_fail == True and B_fail == True:
        winner = 0
    elif A_fail == True and B_fail == False:
        winner = 'B'
    elif A_fail == False and B_fail == True:
        winner = 'A'
    else:
        if cnt_A > cnt_B:
            winner = 'B'
        elif cnt_A == cnt_B:
            winner = 0
        else:
            winner = 'A'

    print('#{} {}'.format(tc, winner))

