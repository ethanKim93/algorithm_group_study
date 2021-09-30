import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, num = input().split()

    result = ''
    for i in range(len(num)-1, -1, -1):
        n16 = int(num[i], 16)
        for j in range(4):
            result = str((n16 >> j) & 1) + result
    print('#{} {}'.format(tc, result))