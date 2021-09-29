def Bbit_print(i):
    result=''
    for j in range(8):
        if i & (1<<j):
            result = '1'+result
        else:
            result = '0'+result
    return result
a = 0x01020304
for i in range(0,4):
    print(Bbit_print((a >> i*8) & 0xff))