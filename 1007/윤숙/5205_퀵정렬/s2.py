import sys

sys.stdin = open('input.txt')

# 현종일 (최종)
def partition(arr, l, r):
    p = arr[l]
    i, j = l, r

    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i < j :
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]
    return j

def quickSort(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        quickSort(arr, l, s - 1)
        quickSort(arr, s + 1, r)

for tc in range(1, int(input())+1):
    N = int(input())
    input_data = list(map(int, input().split()))

    quickSort(input_data, 0, len(input_data)-1)
    print('#{} {}'.format(tc, input_data[N//2]))