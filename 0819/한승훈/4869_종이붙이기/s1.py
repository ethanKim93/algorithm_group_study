import sys
sys.stdin = open('sample_input.txt')

T = int(input())


def rec(N):  # 점화식 A(n) = A(n-1) + A(n-2)*2
    if N == 10:
        return 1
    elif N == 20:
        return 3
    if N > 20:
        return rec(N-10) + rec(N-20)*2


for tc in range(1, T+1):
    N = int(input())
    cnt = rec(N)
    print('#{} {}'.format(tc, cnt))






