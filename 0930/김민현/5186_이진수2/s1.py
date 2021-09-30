import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):

    N = float(input())
    i = -1
    total = 0.0
    ans = ''

    while i > -13: #-13자리가 넘지 않는다면,
        if total + (2**i) == N: #같아질 경우 출력
            ans += '1'
            break
        elif total + (2**i) < N: #기준값보다 total+2**i 가 작을 경우 더해준다.
            ans += '1'
            total += 2**i
        else:
            ans += '0'
        i -= 1
        if i == -13:
            ans = 'overflow'
    print('#{} {}'.format(tc,ans))