import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    n = float(input())

    pn_str = '' # 정답을 저장할 str
    while 15 > len(pn_str):
        n = n * 2
        if n > 1:
            pn_str += '1'
            n -= 1       # 1보다 커지면 정수부 1 빼기
        elif n == 1:       # 딱 나누어 떨어지면 while문 종료
            pn_str += '1'
            break
        else:           #  아니면 0 저장
            pn_str += '0'

    if len(pn_str) == 15:
        print('#{} {}'.format(tc,'overflow'))
    else:
        print('#{} {}'.format(tc,pn_str))

