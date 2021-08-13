import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int,input().split()))
    for last in range(len(A)-1):
        for ind in range(len(A)-1,last,-1):
            if (A[ind-1] < A[ind]) and not last%2:
                A[ind-1], A[ind] = A[ind], A[ind-1]
            if (A[ind-1] > A[ind]) and last%2:
                A[ind-1], A[ind] = A[ind], A[ind-1]
    print('#{}'.format(tc), end=' ')
    for i in range(10):
        print(A[i], end=' ')
    print()
