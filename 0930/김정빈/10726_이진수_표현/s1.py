import sys
sys.stdin = open("input.txt")
#10726. 이진수 표현
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    m2 = bin(M)[2:][::-1]
    res = 'ON'
    if len(m2) >= N:
        if '0' in m2[:N]:
            res = 'OFF'
    elif len(m2) < N:
        res = 'OFF'
    print('#{} {}'.format(tc, res))