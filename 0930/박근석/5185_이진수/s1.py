import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = input().split()
    arr = ''

    for i in range(len(M)):
        word = '0x' + M[i]
        for j in range(3, -1, -1):
            arr += "1" if (1 << j) & int(word, 16) else "0"
    print('#{} {}'.format(tc, arr))
