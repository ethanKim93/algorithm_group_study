# 문자열 뒤집기


def backward(s):
    s_li = []
    for char in s:
        s_li += [char]

    str_len = 0
    for _ in s:
        str_len += 1

    n = str_len // 2

    for i in range(n):
        temp = s_li[i]
        s_li[i] = s_li[-i-1]
        s_li[-i-1] = temp

    result = ''
    for char in s_li:
        result += char

    return result


print(backward('hello world'))