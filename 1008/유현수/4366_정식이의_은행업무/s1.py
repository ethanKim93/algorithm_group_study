import sys
sys.stdin = open('sample_input.txt')


def look_back(b, t):                                    # 이진수 문자열과 삼진수 리스트를 인자로 받는다
    len_b, len_t = len(b), len(t)                       # 이진수 문자열과 삼진수 리스트의 길이
    int_b = int(b, 2)                                   # 이진수 문자열을 10진수로 변환하여 저장

    for i in range(len_b):
        tmp_b = int_b ^ (1 << i)                        # 비트연산으로 이진수의 각 자리 수를 하나씩 바꾼다.
        for j in range(len_t):                          # 3진수 리스트 각 자리 수를 돌면서
            for k in range(3):                          # 0, 1, 2 중
                if int(trinary[j]) != k:                # 현재 값과 다른 것만 선택
                    tmp_t = trinary[:]                  # tmp_t에 3진수 리스트 복사
                    tmp_t[j] = str(k)                   # 선택한 값으로 바꾸기
                    int_t = int(''.join(tmp_t), 3)      # tmp_t를 10진수로 변환
                    if tmp_b == int_t:                  # 한 자리만 바꾼 이진수와 삼진수가 같으면
                        return tmp_b                    # 해당 값을 반환


T = int(input())
for tc in range(1, T+1):
    binary = input()            # 문자열로 입력받기
    trinary = list(input())     # 문자열 원소로 이루어진 리스트로 입력받기

    print('#{} {}'.format(tc, look_back(binary, trinary)))

