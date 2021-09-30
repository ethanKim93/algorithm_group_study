import sys
sys.stdin = open('input.txt')

def check(N):
    cnt = 0
    ans = ''
    while N:
        cnt += 1
        if cnt > 12:
            return 'overflow'
        if N < (2 ** -cnt):
            ans += '0'
        else:
            N -= (2 ** -cnt)
            ans += '1'
    return ans

for tc in range(1, int(input())+1):
    N = float(input())
    print('#{} {}'.format(tc, check(N)))