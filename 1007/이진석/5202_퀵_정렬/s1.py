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


def quick_sort(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        quick_sort(arr, l, s - 1)
        quick_sort(arr, s + 1, r)
    return arr


for tc in range(1, int(input())+1):
    N = int(input())
    nums = list(map(int, input().split()))
    result = quick_sort(nums, 0, len(nums)-1)
    print('#{} {}'.format(tc, result[N//2]))
