def bit_print(i):
    result = ""
    for j in range(8):
        if i & (1 << j):
            result = '1' + result
        else:
            result = '0' + result
    return result

a = 0x10
x = 0x01020304
print(a)
print(x)
for i in range(0, 4):
    # x >> i * 8 는 8개의 비트를 옮기는 행위이므로, 16진수로 표현된 수의 2자리를 옮기는 행위와 같다.
    # 또한 0xff는 11111111로, 16진수의 가장 마지막 두자리와 비교하기 위한 수단으로,
    # (x >> i * 8) & 0xff 는 16진수의 가장 마지막 두자만 보고, i에 따라 2자리씩 옮기면서 본다는 행위이다.
    # 따라서 04, 03, 02, 01을 보기 때문에 00000100 0000011 0000010 0000001이 출력된다.
    print(bit_print((x >> i * 8) & 0xff))