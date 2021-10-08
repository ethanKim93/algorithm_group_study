import sys
sys.stdin = open('sample_input.txt')


def qsort(arr, start, end):
    if start >= end:
        return

    pivot = start # 첫번째를 피벗으로 지정
    left, right = start + 1, end

    while left <= right: # 피벗보다 작은 데이터를 찾을 때까지 반복
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[right], arr[left] = arr[left], arr[right]

        qsort(arr, start, right - 1)
        qsort(arr, right + 1, end)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    qsort(nums, 0, len(nums)-1)
    print(nums)