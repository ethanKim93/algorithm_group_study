import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()

    new_A = A.replace(B, 'B')
    print('#{} {}'.format(tc, len(new_A)))