#숫자 => 문자
def itoa(num):
    li = []
    m = ''
    res = ''

    if num < 0:
        num *= -1
        m += '-'

    if num == 0:
        return '0'

    while num > 0:
        n = num % 10
        li.append(chr(n + 48))
        num = num // 10
        res = "".join(li[::-1])

    return m+res

print(itoa(-103))