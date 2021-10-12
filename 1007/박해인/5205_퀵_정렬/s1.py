# Python 3초 시간초과 Hoarse-Partition
import sys
sys.stdin = open('sample_input.txt')


def partition(arr, l, r):
    p = arr[l]
    i, j = l, r
    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j


def quick_sort(arr, l , r):
    if l < r:
        pivot = partition(arr, l, r)
        quick_sort(arr, 1, pivot-1)
        quick_sort(arr, pivot+1, r)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    quick_sort(data, 0, len(data)-1)

    print('#{} {}'.format(test_case, data[N//2]))
