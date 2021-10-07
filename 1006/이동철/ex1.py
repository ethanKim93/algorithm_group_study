'''
11, 45, 23, 81, 28, 34
11, 45, 22, 81, 23, 34, 99, 22, 17, 8
1, 1, 1, 1, 1, 0, 0, 0, 0, 0
'''


def quick_sort1(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort1(lesser_arr) + equal_arr + quick_sort1(greater_arr)


def quick_sort2(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)


def quick_sort3(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort3(array, start, right - 1)
    quick_sort3(array, right + 1, end)


arr = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
print(quick_sort1(arr))
# 첫번째 것은 새로운 인덱스를 만들어서 사용하는 것이기에 프린트로 함수를 입력해서 출력해야한다.
quick_sort2(arr)
print(arr)
quick_sort3(arr, 0, len(arr) - 1)
print(arr)
