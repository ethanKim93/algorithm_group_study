import sys
sys.stdin = open('input.txt')

def check(M):
    i = 0
    while i < N:
        if M%2 == 0:
            return False
        else:
            M //= 2
            i += 1
    return True


TC = int(input())

for tc in range(1,TC+1):
    N, M = map(int, input().split())

    if check(M):
        result = 'ON'
    else:
        result = 'OFF'
    print('#{} {}'.format(tc, result))