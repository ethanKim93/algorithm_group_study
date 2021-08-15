def itoa(x):
    str = list()
    while True:
        y = x % 10
        str.append(chr(y + ord('0')))
        x //= 10
        if x == 0:
            break
        if x < 0:
            break

    str = str[::-1]
    str = "".join(str)
    if x < 0:
        str += '-'
    return str

print(type(itoa(123)))
print(itoa(123))
print(type(itoa(0)))
print(itoa(0))
print(type(itoa(-123)))
print(itoa(123))
