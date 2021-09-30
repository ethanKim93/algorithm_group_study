import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    binV = format(M, 'b')

    if binV[-N:] == '1'*N:
        print('#{} {}'.format(tc, 'ON'))
    else:
        print('#{} {}'.format(tc, 'OFF'))