def my_atoi(num):
    str_num = ''
    if num == 0:
        return '0'
    while num != 0:
        if num < 0:
            num = -num
            str_num += chr(32)
        num_s = num % 10 + 48
        num = num // 10
        str_num += chr(num_s)
    if str_num[0] == ' ':
        str_num.replace(' ', '')
        str_num = str_num[::-1]
        return '-' + str_num
    return str_num[::-1]

num = int(input())
print(my_atoi(num))