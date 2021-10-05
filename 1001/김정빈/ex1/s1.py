#선택 정렬 함수(SelectionSort)를 재귀적 알고리즘으로 작성해 보시오

arr = [88, 12, 46, 48, 32, 65, 48, 1, 989, 23, 4, 89]
"""
idx = 범위 지정해 주는 수
minI = 가장 작은 값의 위치
"""
def Recurse_SelectionSort(idx, arr):
    minI = idx
    if idx == len(arr):
        return 1 #재귀종료
    else:
        for i in range(idx+1, len(arr)):
            if arr[i] < arr[minI]:
                minI = i
        arr[idx], arr[minI] = arr[minI], arr[idx]
        return Recurse_SelectionSort(idx+1, arr)
