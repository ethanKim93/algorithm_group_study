# 최종코드 (안재현)

import sys
sys.stdin=open('input.txt')
T = int(input())
for tc in range(T):
    N = float(input())
    result = ''
    arr = ['', '']
    while arr[1] != '0' and len(result) < 13:
        N *= 2
        arr = str(N).split('.')
        if arr[0] == '1':
            result += '1'
        else:
            result += '0'
        N = float('0.'+arr[1])
    if len(result) == 13:
        print('#{} overflow'.format(tc + 1))
    else:
        print('#{} {}'.format(tc + 1, result))


































# print()
# print(2&(1<<0), bin(1<<0))
# print(2&(1<<1), bin(1<<1))
# print(2&(1<<2), bin(1<<2))
# print(2&(1<<3), bin(1<<3))
# print()
# print(2<<0,2<<2, bin(2<<0), bin(2<<2))
#
