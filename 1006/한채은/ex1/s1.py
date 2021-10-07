arr = [23, 65, 78, 99, 234, 51, 12, 18, 29, 34, 38]


def quickSorting(arr, start, end):  # 정렬할 배열, 배열의 시작 인덱스, 마지막 인덱스
    if start >= end:    # 재귀함수 끝내주기 위한 base case
        return

    pivot = start  # 맨 왼쪽 값
    left = start + 1  # arr[pivot]보다 큰 값을 저장할 left 인덱스
    right = end  # arr[pivot]보다 작은 값을 저장할 right 인덱스

    while left <= right:  # left와 right가 엇갈리지 않을 때까지
        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        # while문을 빠져나오면 arr[left]와 arr[right]는 각각 arr[pivot]보다 큰 값, 작은 값을 갖는다.

        if left > right:    # left와 right가 엇갈린 경우
            arr[right], arr[pivot] = arr[pivot], arr[right]

        else:
            arr[left], arr[right] = arr[right], arr[left]

        # 배열을 pivot 기준으로 두개로 분할 후, 분할 된 배열 모두 퀵정렬 실행

        quickSorting(arr, start, right-1)
        quickSorting(arr, right+1, end)

quickSorting(arr, 0, len(arr)-1)
print(arr)

