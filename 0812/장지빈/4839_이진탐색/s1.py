import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    Astart = Bstart = 1
    Aend = Bend = P
    Acnt = Bcnt = 0

    while Astart < Aend:
        middle = (Astart + Aend) // 2
        Acnt += 1
        if A < middle:
            Aend = middle
        elif A > middle:
            Astart = middle
        else:
            break
    while Bstart < Bend:
        middle = (Bstart + Bend) // 2
        Bcnt += 1
        if B < middle:
            Bend = middle
        elif B > middle:
            Bstart = middle
        else:
            break

    result = 0
    if Acnt < Bcnt:
        result = 'A'
    elif Acnt > Bcnt:
        result = 'B'
    else:
        pass

    print('#{} {}'.format(tc, result))