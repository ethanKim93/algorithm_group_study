def Bbit_print(i):
    output = ""
    # 부호화-크기표현 : -( 2^7 - 1 ) ~ +( 2^7 - 1 )
    # 1의 보수 표현범위 : -( 2^7 - 1 ) ~ +( 2^7 - 1 )
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output)

for i in range(-5, 6):
    print('{} = '.format(i) ,end='')
    Bbit_print(i)