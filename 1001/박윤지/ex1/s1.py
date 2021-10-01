# 선택정렬함수를 재귀적 알고리즘으로 작성해 보세요.

def selectionSort(arr, n, k):  # n = len(arr)
    if k == n-1:
        return arr
    else:
        minV = arr[k]
        minI = k
        for j in range(k+1, n):
            if minV > arr[j]:
                minV = arr[j]
                minI = j
        arr[k], arr[minI] = arr[minI], arr[k]
        # print(arr)
        return selectionSort(arr, n, k+1)

li = [3, 1, 2]
print(selectionSort(li, len(li), 0))
