# 배열의 데이터를 퀵 정렬하는 함수를 작성하고 테스트해보세요


# Hoare-Partition 알고리즘

def quicksort(l, r):
    global arr
    if l < r:
        s = partition(l, r)
        quicksort(l, s - 1)
        quicksort(s + 1, r)

def partition(l, r):
    global arr
    p = arr[l]
    i = l
    j = r
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



l = 0
r = len(arr)
quicksort(l, r-1)
print(arr)