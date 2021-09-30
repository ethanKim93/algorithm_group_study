import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, T+1):
    N = float(input())                          # float형으로 저장
    result = ''                                 # 빈 문자열 생성
    cnt = 0                                     # 자릿수 기록
    print('#{}'.format(tc), end=' ')

    while N != 0 and cnt < 13:                  # 0이거나 13자리 이상이면 중단
        N *= 2
        cnt += 1                                # 자릿수 카운트
        if N >= 1:                              # 2를 곱해서 1이상이면 현재 자리수 1
            result += '1'
            N -= 1
        else:                                   # 2를 곱해서 1미만이면 현재 자리수 0
            result += '0'

    if cnt <= 12:
        print(result)
    else:
        print('overflow')