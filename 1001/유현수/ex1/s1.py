def selection_sort(arr, i):
    n = len(arr)
    if i == n:
        return arr
    else:
        min_idx = i
        for j in range(i, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return selection_sort(arr, i+1)


li = [64, 25, 10, 22, 11]
print(selection_sort(li, 0))