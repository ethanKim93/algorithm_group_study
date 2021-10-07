input_data = [11, 45, 23, 81, 7, 34, 99, 22, 17, 8]
length = len(input_data)

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

# def partition(arr, l, r):
#     pivot = arr[r]
#     i = l - 1
#     for j in range(l, r-1):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i+1], arr[r] = arr[r], arr[i+1]
#     return i+1

def quickSort(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        quickSort(arr, l, s-1)
        quickSort(arr, s+1, r)


quickSort(input_data, 0, length-1)

print(input_data)


