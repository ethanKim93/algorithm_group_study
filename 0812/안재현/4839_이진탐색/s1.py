import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(0, T):
    P, A, B = map(int, input().split())
# A는 P까지 찾기, B는 1에서부터 찾기
    Acnt = Bcnt = 0
    start = 1
    PA = PB = end = P
    while PA == A:
        PA = int((start + end) / 2)
        if A < PA:
            Acnt += 1
            end = PA
        elif A > PA:
            Acnt += 1
            start = PA

    while PB == B:
        PB = int((start + end) / 2)
        if B > PB:
            Bcnt += 1
            start = PB
        elif B < PB:
            Bcnt += 1
            end = PB

    if Acnt > Bcnt:
        print(Acnt)
        print(Bcnt)
        print('#{} A'.format(tc+1))
    elif Acnt < Bcnt:
        print(Acnt)
        print(Bcnt)
        print('#{} B'.format(tc+1))
    else:
        print(Acnt)
        print(Bcnt)
        print('#{} 0'.format(tc+1))