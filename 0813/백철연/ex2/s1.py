#print(chr(48))
#print(chr(49))
def itoa(num):

    if num < 0:
        num = -num
        result = ''
        while num > 0:
            result = chr(48 + num%10) + result
            num = num//10
        return '-' + result

    elif num > 0:
        result = ''
        while num > 0:
            result = chr(48 + num%10) + result
            num = num//10
        return result

print(itoa(123456))