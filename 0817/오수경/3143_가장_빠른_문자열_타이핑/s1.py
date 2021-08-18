import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()

    cnt = 0

    a = 0
    while a < len(A):
        if A[a:a+len(B)] == B and len(A[a:a+len(B)]) >= len(B):
            cnt += 1
            a = a+len(B)

        else:
            cnt += 1
            a += 1

    print('#{} {}'.format(tc, cnt))

