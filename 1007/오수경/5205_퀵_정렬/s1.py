import sys
sys.stdin = open('sample_input.txt')


def Lomuto(A, l, r):
    x = A[r]
    i = l - 1

    for j in range(l, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A, l, r):
    if l < r:
        s = Lomuto(A, l, r)

        quick_sort(A, l, s - 1)
        quick_sort(A, s + 1, r)
    return A


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    A = quick_sort(A, 0, N-1)

    print('#{} {}'.format(tc, A[N//2]))



