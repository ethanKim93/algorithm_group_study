num = int(input())
str_num = ''


def itoa(number, string):
    list_temp = []
    if number < 0:
        number *= (-1)
        while number:
            temp = number % 10
            char = chr(temp + 48)

            list_temp.insert(0, char)
            number //= 10
        list_temp.insert(0, '-')
    else:
        while number:
            temp = number % 10
            char = chr(temp + 48)

            list_temp.insert(0, char)
            number //= 10
    string = ''.join(list_temp)
    print(string)


itoa(num, str_num)
