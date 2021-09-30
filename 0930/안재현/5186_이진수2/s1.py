import sys
sys.stdin = open('sample_input.txt')

# 최종코드 (안재현)
T = int(input())
for tc in range(T):
    N = float(input())
    result = ''                 # 이진수를 출력할 값
    # while True:               # 13자리까지 출력, break문이 있기에 True도 가능
    while len(result) < 13:     # 소숫점이 13자리 이상일 경우 overflow 출력이므로
        N *= 2 # 0.625 1.25
        arr = str(N).split('.') # 소수점을 기준으로 정수값과 실수값을 문자열 리스트로 나눔
        if arr[0] == '1':       # 정수값이 1일경우 자릿수 1
            result += '1'
        else:
            result += '0'       # 0일 경우 자릿수 0
        N = float('0.'+arr[1])  # 남은 실수값 앞에 0. 을 붙인 후 str을 float로 변경

        if arr[1] == '0':       # 소수값이 0일 경우 종료
            break
        if len(result) == 13:   # 2진수가 13자리 이상일 경우 결과를 overflow로 변경 후 종료
            result = 'overflow'
            break

    print('#{} {}'.format(tc + 1, result))
