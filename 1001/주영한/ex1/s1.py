def SelectionSort(arr, start_idx):
    if start_idx == len(arr) - 1:
        return

    maxIdx = start_idx
    for i in range(start_idx, len(arr)):
        if arr[maxIdx] < arr[i]:
            maxIdx = i
    arr[start_idx], arr[maxIdx] = arr[maxIdx], arr[start_idx]
    return SelectionSort(arr, start_idx + 1)


arr = [1, 3, 6, 2, 7, 5, 4]
print(arr)
SelectionSort(arr, 0)
print(arr)