def Itoa(num):
    if num > 0:
        it_li = []
        while num >0:
            N = num % 10
            it_li.insert(0, chr(N+48))
            num = int(num/10)
        str_num = ''.join(it_li)
    elif num < 0:
        it_li = ['-']
        num = abs(num)
        while num >0:
            N = num % 10
            it_li.insert(1, chr(N+48))
            num = int(num/10)
        str_num = ''.join(it_li)
    else:
        str_num = '0'
    return str_num

print(Itoa(-1358))
print(Itoa(1359))
print(Itoa(0))