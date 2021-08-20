import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())//10
    p = 1

    for i in range(1, N+1):
        if i % 2:
            p = (p*2) - 1
        else:
            p = (p*2) + 1
    print('#{} {}'.format(tc, p))


