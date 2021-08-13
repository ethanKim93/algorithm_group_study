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


print(my_itoa(123))


def my_atoi(s):
    result = 0

    s_len = 0
    for _ in s:
        s_len += 1

    for i in range(s_len):
        temp = ord(s[i]) - 48
        result += temp * (10 ** (s_len - i - 1))

    return result


print(my_atoi('123'))