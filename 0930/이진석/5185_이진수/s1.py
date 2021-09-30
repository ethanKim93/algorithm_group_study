import sys
sys.stdin = open('sample_input.txt')

for tc in range(1, int(input())+1):
    N, hexa = input().split(' ')            # N : 자릿수, hexa : 16진수
    answer = ''                             # 앞자리의 0도 출력하기 위해서 문자열 형태로 출력을 저장
    for i in range(int(N)):                 # 각 자리마다(4bit)
        temp = ''
        # if hexa[i].isdecimal():             # 숫자(0~9)라면 바로 정수로 변환
        #     num = int(hexa[i])
        # else:                               # 문자(A~F)라면 ASCII 변환 후 각 문자에 대응하는 수로 변환
        #     num = ord(hexa[i])-65+10
        num = int(hexa[i]) if hexa[i].isdecimal() else ord(hexa[i])-65+10
        for j in range(4):                  # 4bit
            temp = ('1' if num & (1 << j) else '0') + temp  # 이진수 변환(비트연산)
        answer += temp                      # 출력 저장
    print('#{} {}'.format(tc, answer))