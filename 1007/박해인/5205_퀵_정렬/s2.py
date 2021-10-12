# Lomuto-partition 통과
import sys
sys.stdin = open('sample_input.txt')

def partition(arr, p, r):
    x = arr[r]
    i = p-1

    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def quick_sort(arr, l, r):
    if l < r:
        pivot = partition(arr, l, r)
        quick_sort(arr, l, pivot-1)
        quick_sort(arr, pivot+1, r)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    quick_sort(data, 0, len(data)-1)

    print('#{} {}'.format(test_case, data[N//2]))