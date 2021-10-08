import sys
sys.stdin = open('sample_input.txt')

T = int(input())


def quicksort(arr, low, high):
    def partition(low, high):
        pivot = arr[high]
        left = low  # 값의 시작 범위
        for right in range(low, high):
            if arr[right] < pivot:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1  # 스왑 후 단계를 증가시킨다.
        arr[left], arr[high] = arr[high], arr[left]
        return left

    if low < high:
        pivot = partition(low, high)
        # print("arr : ", arr)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)

    return arr

for tc in range(1,T+1):
    N = int(input())
    array = list(map(int,input().split()))
    res = quicksort(array,0,N-1)
    print('#{} {}'.format(tc,res[N//2]))