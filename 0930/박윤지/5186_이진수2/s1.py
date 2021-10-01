import sys
sys.stdin = open('sample_input.txt', 'r')

def func(N, ans):
    for i in range(1, 13):
        if N >= 2 ** (-i):
            N -= 2 ** (-i)
            ans += '1'
            if N == 0:
                return ans
        else:
            ans += '0'
    if N > 0:
        return 'overflow'
    return ans


T = int(input())

for tc in range(1, T+1):
    N = float(input())
    ans = ''
    print('#{} {}'.format(tc, func(N, ans)))
