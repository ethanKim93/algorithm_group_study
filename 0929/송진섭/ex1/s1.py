"""
0000000111100000011000000111100110000110000111100111100111111001100111
00000010001101
"""


def decimal_changer(a_list):
    result = ''
    for j in a_list:
        n = int(j, 2)
        result += str(n) + ', '
    return result[:-2]


a = input()
bit_num = [a[i:i+7] for i in range(0, len(a), 7)]

ans = decimal_changer(bit_num)
print(ans)