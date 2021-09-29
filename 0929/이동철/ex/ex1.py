def bit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += '1' if i & (1 << j) else '0'
    print(output)


for i in range(-5, 6):
    print('%3d = ' % i, end='')
    bit_print(i)


##################################################


def bit_print(i):
    result = ""
    for j in range(8):
        if i & (1 << j):
            result = '1' + result
        else:
            result = '0' + result
    return result


for i in range(-5, 6):
    print("{} = {}".format(i, bit_print(i)))