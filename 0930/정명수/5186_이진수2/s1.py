import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N = float(input())
    ans = ''
    for i in range(1,13): # 0.10111 2**(-1)+2**(-3)+2**(-4)+2**(-5)
        if N >= 1/(2**i): # 1/2=0.5 1/4 1/8 1/16
            ans += '1'
            N -= 1/(2**i)
        else:
            ans += '0'
        if not N:
            break
    if N:
        print('#{} {}'.format(tc,'overflow'))
    else:
        print('#{} {}'.format(tc,ans))

