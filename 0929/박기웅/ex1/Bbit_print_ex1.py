# 음수는 양수에서 비트 반전 후 +1을 하여 표현됨
def Bbit_print(i):
    output = ''
    # 8자리씩 2진수로 표현
    for j in range(7, -1, -1):
        output += '1' if i & (1 <<j) else '0'
    print(output)

for i in range(-5,6):
    print(f'%3d = ' % i, end='')
    Bbit_print(i) 