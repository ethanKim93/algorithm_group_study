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