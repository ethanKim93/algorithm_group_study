import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    N = len(A)
    M = len(B)
    i = 0
    result = 0

    while i < N:
        if i <= N - M + 1:
            if A[i: i+M] == B:
                i += M
            else:
                i += 1
        else:
            i += 1
        result += 1

    print('#{} {}'.format(tc, result))
