def partition(A, l, r):
    p = A[l] # 피봇 수
    i, j = l, r
    while i <= j:
        while i <= j and A[i] <= p: # 피봇 수 보다 큰 애를 찾아 오른쪽으로 이동
            i += 1
        while i <= j and A[j] >= p: # 작은애를 찾아 왼쪽으로 이동
            j -= 1
        if i<j: # 두 개가 아직 교차되지 않은 상태면 swap
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

def quick_sort(A, l, r):
    if l<r:
        s = partition(A, l, r)
        quick_sort(A, l ,s-1)
        quick_sort(A, s+1, r)

arr = [11, 45, 23, 81, 28, 34]
# arr = [11, 45, 23, 81, 28, 34, 99, 22, 17, 8]
quick_sort(arr, 0, len(arr)-1)
print(arr)