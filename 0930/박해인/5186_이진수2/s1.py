import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = float(input())

    result = ''
    for i in range(-1, -13, -1):
        result += str(int(N // 2 ** i))
        N = N % (2 ** i)

        if N == 0:
            break

    if N != 0:
        result = 'overflow'
    print('#{} {}'.format(test_case, result))
