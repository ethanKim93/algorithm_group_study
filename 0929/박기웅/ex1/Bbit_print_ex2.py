# 받은 숫자 i를 8자리씩 끊어서 2진수로 표현
# Ex. 16을 받으면 00010000

def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (1<<j) else '0'
    print(output, end=' ')

a = 0x10        # 16
x = 0x01020304  # 1*16**6 + 2*16**4 + 3*16**2 + 4*16**0
print(f'%d = ' % a, end='')
Bbit_print(a)
print()
print(f'0%X = ' % x, end='')
for i in range(0, 4):
    # 0xff = 16*15+15 = 255 = 11111111
    # 뒤부터 오른쪽 시프트하여 8자리씩 끊어서 입력
    Bbit_print((x >> i*8) & 0xff )