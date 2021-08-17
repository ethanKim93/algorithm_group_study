def itoa():
    num = int(input())

    if num < 0:
        num = -num
        word = ''
        while num > 0:
            word = chr(48 + num%10) + word
            num = num//10
        return '-' + word


    elif num > 0:
        word = ''
        while num > 0:
            word = chr(48 + num%10) + word
            num = num//10

        return word

    else:
        return '0'

print(itoa())


