import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = float(input())
    ans = ''

    while N:
        N = N*2
        if N >= 1:
            ans += '1'
            N -= 1
        else:
            ans += '0'
        if len(ans) >= 13:
            ans = 'overflow'
            break

    print('#{} {}'.format(tc, ans))