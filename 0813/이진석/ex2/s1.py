def itoa(number, string):
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
    print(string)


def atoi(string):
    number = 0
    for char in string:
        number *= 10
        number += ord(char) - 48
    print(number)

itoa(123, '')
atoi('1234')