# str() 없이 itoa() 구현


def my_itoa(n):
    result = ''
    while n > 0:
        temp = n % 10
        s_temp = chr(temp + 48)
        result = s_temp + result
        n -= n % 10
        n //= 10
    return result


print(my_itoa(100))