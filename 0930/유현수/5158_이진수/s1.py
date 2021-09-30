# import sys
# sys.stdin = open('sample_input.txt')


def bit_print(num):
    for i in range(4):
        if num & (8 >> i):
            print('1', end='')
        else:
            print('0', end='')


T = int(input())
for tc in range(1, T+1):
    M = input()
    N = len(M)
    print('#{}'.format(tc), end=' ')
    for i in range(int(N)):
        n = int(M[i], 16)
        bit_print(n)
    print()
