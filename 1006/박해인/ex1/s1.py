# 연습문제 1 배열의 데이터를 퀵 정렬하는 함수를 작성하고 테스트 해보시오.
def quick_sort(arr, l, r):  # array, left, right
    if l < r:
        pivot = partition(arr, l, r)
        quick_sort(arr, l, pivot-1)
        quick_sort(arr, pivot+1, r)


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

arr = [11, 45, 23, 81, 28, 34]
arr_b = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
arr_c = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
quick_sort(arr, 0, len(arr)-1)
print(arr)  # [11, 23, 28, 34, 45, 81]
quick_sort(arr_b, 0, len(arr_b)-1)
print(arr_b)  # [8, 11, 17, 22, 22, 23, 34, 45, 81, 99]
quick_sort(arr_c, 0, len(arr_c)-1)
print(arr_c)  # [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
