import sys
sys.stdin = open('sample_input.txt')

def partition(arr, start, end):
    pivot = arr[start]
    i = start + 1
    j = end

    while i <= j:
        while i <= j and arr[i] <= pivot:   # i는 pivot보다 큰 값 index
            i += 1
        while i <= j and arr[j] >= pivot:   # j는 pivot보다 작은 값 index
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i] # 작은 값, 큰 값 위치 바꿈
    arr[start], arr[j] = arr[j], arr[start]

    return j


def quick_sort(arr, start, end):
    if start < end:
        mid = partition(arr, start, end)
        quick_sort(arr, start, mid-1)
        quick_sort(arr, mid+1, end)


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    A = list(map(int,input().split()))
    quick_sort(A, 0, N - 1)
    print(A)
    # print('#{} {}'.format(tc, A[N//2]))