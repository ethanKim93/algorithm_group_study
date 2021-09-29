import sys
sys.stdin = open('input.txt')


# 암호코드 정보를 추출
def get_secret_code_info():
    flag = 0
    secret_code_info = ''
    for i in range(N):
        for j in range(M-1, 55, -1):
            if data[i][j] == '1':
                secret_code_info = data[i][j-55:j+1]
                flag = 1
                break
        if flag:
            break
    return secret_code_info


# 암호코드 정보를 슬라이싱해서 암호코드 추출
def get_secret_code(secret_code_info):
    encode = {'0001101': '0',
              '0011001': '1',
              '0010011': '2',
              '0111101': '3',
              '0100011': '4',
              '0110001': '5',
              '0101111': '6',
              '0111011': '7',
              '0110111': '8',
              '0001011': '9'}

    secret_code = ''
    for i in range(len(secret_code_info)//7):
        s = secret_code_info[i*7:i*7+7]
        for key, value in encode.items():
            if s == key:
                secret_code += value

    return secret_code

# 검증코드 추출
def get_verification_code(secret_code):
    odd_sum, even_sum = 0, 0
    for i in range(0, 7):
        if i % 2:  # 홀수
            even_sum += int(secret_code[i])
        else:  # 짝수
            odd_sum += int(secret_code[i])
    for v in range(0, 10):
        if (odd_sum * 3 + even_sum + v) % 10 == 0:
            v_code = v
            return v_code

# 올바른 암호코드인가?
def is_secret_code(v_code, secret_code):
    last_number = int(secret_code[-1])

    if v_code == last_number:
        return True
    else:
        return False


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())  # M-80개 N-16줄
    data = [input() for _ in range(N)]

    v_code = get_verification_code(get_secret_code(get_secret_code_info()))
    secret_code = get_secret_code(get_secret_code_info())

    result = 0
    if is_secret_code(v_code, secret_code) == 1:
        for i in secret_code:
            result += int(i)
    else:
        result = 0

    print('#{} {}'.format(test_case, result))


