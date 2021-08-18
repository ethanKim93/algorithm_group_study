import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    cnt = 0
    A_len = len(A)
    B_len = len(B)
    j = 0
    i = 0
    while i < A_len and j < B_len:
        if A[i] != B[j]:
            i -= j
            j = -1
        i += 1
        j += 1
        if j == len(B):
            cnt += 1
            i += len(B)
            j = 0
    ans = len(A) + cnt - len(B)*cnt

    print('#{} {}'.format(tc, ans))
