# import sys
# sys.stdin = open('sample_input.txt', 'r')
#
# dict16_2 = {
#     '0': '0000',
#     '1': '0001',
#     '2': '0010',
#     '3': '0011',
#     '4': '0100',
#     '5': '0101',
#     '6': '0110',
#     '7': '0111',
#     '8': '1000',
#     '9': '1001',
#     'A': '1010',
#     'B': '1011',
#     'C': '1100',
#     'D': '1101',
#     'E': '1110',
#     'F': '1111',
# }
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, N16 = input().split()  # 둘 다 string
#
#     ans = ''
#     for i in N16:
#         ans += dict16_2[i]
#     print('#{} {}'.format(tc, ans))


##################################

# import sys
# sys.stdin = open('sample_input.txt', 'r')
#
#
# def Bbit_print(i):
#     output = ''
#     for j in range(3, -1, -1):
#         output += '1' if i & (1 << j) else '0'
#     return output
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, hex_str = input().split()
#
#     ans = ''
#     for k in hex_str:
#         k = int(k, 16)  # 16진수를 10진수로 변환
#         ans += Bbit_print(k)
#     print('#{} {}'.format(tc, ans))


#####################################

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

def binary(n):
    bi = ''
    for _ in range(4):
        bi = str(n % 2) + bi
        n //= 2
    return bi

for tc in range(1, T + 1):
    N, hexa = input().split()
    bi_num = ''
    for i in range(int(N)):
        bi_num += binary(ord(hexa[i]) if ord(hexa[i]) > 64 else ord(hexa[i]) - 48)
    print('#{} {}'.format(tc, bi_num))