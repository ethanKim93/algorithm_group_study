# 선택정렬
def selection_sort1(arr):
    for i in range(len(arr) - 1):
        tmp = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[tmp]:
                tmp = j
        arr[i], arr[tmp] = arr[tmp], arr[i]
    return arr


# 선택정렬 + 재귀?
def selection_sort2(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            return selection_sort2(arr)
    return arr


TC1 = [11, 3, 6, 4, 12, 1, 2]
TC2 = [11, 3, 6, 4, 12, 1, 2]
print(selection_sort1(TC1))
print(selection_sort2(TC2))
