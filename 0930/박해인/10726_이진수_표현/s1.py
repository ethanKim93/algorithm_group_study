import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    flag = 1
    for i in range(N):
        if M & (1 << i) == 0:
            flag = 0
            break

    if flag:
        result = 'ON'
    else:
        result = 'OFF'

    print('#{} {}'.format(test_case, result))