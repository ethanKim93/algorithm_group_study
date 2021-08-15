def itoa(number):
    list_temp = []
    if number < 0:  # 음수일때
        number *= (-1)
        while number:
            list_temp.insert(0, chr(number % 10 + 48))
            number //= 10
        list_temp.insert(0, '-')
    else:  # 양수일때
        while number:
            list_temp.insert(0, chr(number % 10 + 48))
            number //= 10
    string = ''.join(list_temp)
    return string


def atoi(string):
    number = 0
    minus = 0
    if string[0] == '-':  # 음수인경우 확인
        minus = 1
        string = string[1:]
    for char in string:  # 0번인덱스(가장 큰 자리수) 부터 ascii 변환을 하면서 숫자로 바꿔주고 10을 곱해준다
        number *= 10
        number += ord(char) - 48
    if minus:  # 음수일 경우 -1을 곱해준다
        number *= (-1)
    return number


print(itoa(123), type(itoa(123)))
print(itoa(-123), type(itoa(123)))
print(atoi('1234'), type(atoi('1234')))
print(atoi('-1234'), type(atoi('1234')))
