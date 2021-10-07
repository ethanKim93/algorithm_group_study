
# Hoare Partition
def partition(arr, l, r):
    p = arr[l] # p: 피벗 값 할당
    i, j = l, r
    while i <= j:
        while i <= j and arr[i] <= p: i+=1
        while i <= j and arr[j] >= p: j-=1
        if i < j: arr[i], arr[j] = arr[j], arr[i]
    # i와 j 가 크로스되면 피벗(arr[l])보다 작은 값이 왼쪽에 위치해야 하므로 j와 위치 변경
    arr[l], arr[j] = arr[j], arr[l]
    # 피벗의 위치 리턴
    return j

def quick_sort(arr, l, r):
    if l < r:
        # s = 확정된 피벗의 위치
        s = partition(arr, l, r)
        # 피벗보다 왼쪽의 배열 정렬
        quick_sort(arr, l, s-1)
        # 피벗보다 오른쪽의 배열 정렬
        quick_sort(arr, s+1, r)


arr = [11, 45, 23, 81, 28, 34]
arr = [11, 45, 23, 81, 28, 34, 99 , 22, 17, 8]
# arr = [1,1,1,1,1,0,0,0,0,0,0]

quick_sort(arr, 0, len(arr)-1)
print(arr)