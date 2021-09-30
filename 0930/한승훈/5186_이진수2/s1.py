import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    num = float(input())
    ans = ''
    i = 1
    while i <= 13:
        if num <= 0:
            print('#{} {}'.format(tc, ans))
            break
        if num >= 2**-i:
            num -= 2**-i
            ans += '1'
        else:
            ans += '0'
        i += 1
    else:
        print('#{} overflow'.format(tc))