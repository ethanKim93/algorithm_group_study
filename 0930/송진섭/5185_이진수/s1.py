import sys
sys.stdin = open('sample_input.txt')


def Bbit_print(i):
    output = ''
    for j in range(3, -1, -1):                      # 4자리
        output += '1' if i & (1 << j) else '0'      # i의 j자리 비트가 1인지 확인
    return output


T = int(input())
for tc in range(1, T+1):
    N, hex_str = input().split()
    bit_num = ''                                    # 2진수로 저장할 변수

    for i in hex_str:
        i = int('0x'+i, 16)                         # 16진수를 10진수로 변경
        bit_num += Bbit_print(i)                    # 10진수 하나씩 4비트 2진수로 변경
    print('#{} {}'.format(tc, bit_num))
