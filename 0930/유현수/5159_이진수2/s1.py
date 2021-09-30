import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    ans = ''
    for i in range(1, 13):
        tmp = 1 / (2**i)
        if N >= tmp:
            N -= tmp
            ans += '1'
            if not N:
                print('#{} {}'.format(tc, ans))
                break
        else:
            ans += '0'
    else:
        print('#{} overflow'.format(tc))