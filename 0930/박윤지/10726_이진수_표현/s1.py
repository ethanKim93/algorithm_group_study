import sys
sys.stdin = open('input.txt', 'r')


def Bbit_print(i, n):
    for j in range(0, n):
        if i & (1 << j):
            pass
        else:
            return 'OFF'
    return 'ON'


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, Bbit_print(M, N)))