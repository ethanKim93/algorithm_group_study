def selectSort(arr):

    if arr:
        x = min(arr)
        arr.remove(x)
        return [x] + selectSort(arr)
    else:
        return []

arr = [1,3,2,5,0,9,8]
print(selectSort(arr))