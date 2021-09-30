"""
0F97A3
01D06079861D79F99F
"""


def Bbit_print(i):
    output = ''
    for j in range(3, -1, -1):
        output += '1' if i & (1 << j) else '0'
    return output


def decimal_changer(a_list):
    result = ''
    for j in a_list:
        n = int(j, 2)
        result += str(n) + ', '
    return result[:-2]


hex_list = list(input())
bit_num = ''

for i in hex_list:
    i = int('0x'+i, 16)
    bit_num += Bbit_print(i)

bit_list = [bit_num[i:i+7] for i in range(0, len(bit_num), 7)]
print(decimal_changer(bit_list))


