import sys
sys.stdin = open('input.txt')

def num_bit(num, N):
    global output
    for j in range(N-1, -1, -1):
        if num & (1 << j):
            output.append('1')
        else:
            output.append('0')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    output = []
    num_bit(M, N)
    if ''.join(output) == '1'*N:
        print('#{} ON'.format(tc))
    else:
        print('#{} OFF'.format(tc))