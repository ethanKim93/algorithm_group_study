# 숫자를 문자열로
# chr() : ASCII 코드 값 -> 문자
# ord() : 문자 ->  ASCII 코드 값

def int_to_string(number):
    answer = []
    result = []
    if number > 0: # 양수일 때
        while number > 0:
            result.append(chr((number % 10) + 48))  # 48
            number = number // 10
            answer = ''.join(result[::-1])

    elif number == 0:
        return '0'

    else:  # 음수일 때
        number = number * -1
        while number > 0:
            result.append(chr((number % 10) + 48))  # 48
            number = number // 10
            answer = '-' + ''.join(result[::-1])

    return answer

print(int_to_string(719))
print(int_to_string(0))
print(int_to_string(-423))
print(type(int_to_string(66324)))