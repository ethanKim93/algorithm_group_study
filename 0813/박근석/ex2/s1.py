def itoa(number):
    b = 0
    if number < 0:
        number = -1*number
        b = 1

    list_a = []
    while number > 0:
        a = number%10
        number //=10
        list_a.append(a)
    list_a.reverse()

    new_str = ''
    for i in list_a:
        new_str += chr(i+48)

    if b == 1:
        new_str = '-' + new_str
    return new_str

print(itoa(123))
print(type(itoa(123)))
print(itoa(-123))
print(type(itoa(-123)))


