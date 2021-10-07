import sys
sys.stdin = open('input.txt')


def quicksort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quicksort(A, l, s-1)
        quicksort(A, s+1, r)


def partition(A, l, r):
    p = A[l]
    i, j = l, r
    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


T = int(input())
for tc in range(1, T+1):
    A = list(map(int, input().split()))
    quicksort(A, 0, len(A)-1)
    print('#{} {}'.format(tc, A))