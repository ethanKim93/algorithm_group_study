import sys

sys.stdin = open('sample_input.txt', 'rt', encoding='UTF8')

T = int(input())
for tc in range(0, T):
    R = input()
    A = input()
    C = ''
    count = 0
    search = 0
    while search + len(R) <= len(A):
        for i in range(len(R)):
            C += A[i + search]
        if C == R:
            count = 1
            search += 1
            C = ''
        else:
            search += 1
            C = ''
    print('#{} {}'.format(tc+1, count))
