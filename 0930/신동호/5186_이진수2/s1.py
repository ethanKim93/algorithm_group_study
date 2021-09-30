import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = float(input())
    result = ''
    n = 0
    while N:
        if n == 12:
            result = 'overflow'
            break
        N *= 2
        result += str(int(N))
        N %= 1
        n += 1
    print('#{} {}'.format(tc, result))