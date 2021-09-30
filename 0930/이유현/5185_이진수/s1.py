import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, hex_str = input().split()

    hex_dec = []
    for hex in hex_str:
        hex_dec.append(int(hex, 16))

    bin_str = ''
    for bin in hex_dec:
        bin_str += '{0:b}'.format(bin).zfill(4)

    print('#{} {}'.format(tc, bin_str))