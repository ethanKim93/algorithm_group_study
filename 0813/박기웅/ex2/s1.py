def itoa(integers):
    to_str = ''
    if not integers:
        return integers
    elif integers < 0:
        integers *= -1
        while (integers):
            to_str += chr(48 + integers % 10)
            integers //= 10
        return '-'+to_str[::-1]
    else:
        while(integers):
            to_str += chr(48+integers%10)
            integers //= 10
        return to_str[::-1]

print(itoa(0))
print(itoa(-123))
print(3402)
