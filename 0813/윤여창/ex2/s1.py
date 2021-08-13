def change(number):
    bin=''
    if number > 0:
        while number >= 1:
            num = number % 10
            number = number // 10
            bin = chr(num+48) + bin
        return bin
    elif number < 0:
        number = -number
        while number >= 1:
            num = number % 10
            number = number // 10
            bin = chr(num+48) + bin
        return '-' + bin
    else:
        return chr(number+48)

print(change())
