import sys
sys.stdin = open('sample_input.txt')

for tc in range(1, int(input())+1):
    N = float(input())      # N을 실수형으로 받음
    bins = ''               # 저장할 소수점 이하 이진수
    i = 0                   # 이진수의 소수점 계산을 위한 i
    while N:                # N이 0이 되면 루프 종료
        i -= 1              
        if i < -12:         # 소수점 아래 12자리 이내가 아니면 종료
            bins = 'overflow'
            break
        if N-2**i >= 0:     # 2^i를 뺏을 때 0 이상이면 빼고 1을 append
            bins += '1'
            N -= 2**i
        else:               # 0 미만이면 0을 append
            bins += '0'
    print('#{} {}'.format(tc, bins))
            