import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    li_16 = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
    N, num = input().split()
    ans = ''
    for i in range(int(N)):
        convert16 = int(num[i], 16)
        ans += li_16[convert16]
    # z = int('0100', 2)
    # z1 = int('1011', 2)
    # print(z, z1)

    print('#{} {}'.format(tc, ans))