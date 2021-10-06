# QuickSort 구현하기
# Hoare-Partition 알고리즘

# 11 45 23 81 28 34
# 11 45 22 81 23 34 99 22 17 8
# 1 1 1 1 1 0 0 0 0 0

def quickSort(l, r):
    global A
    if l < r:
        s = partition(l, r)
        quickSort(l, s-1)
        quickSort(s+1, r)

def partition(l, r):
    global A
    p = A[l]
    i = l
    j = r
    while i <= j:
        while i <= j and A[i] <= p: i += 1
        while i <= j and A[j] >= p: j -= 1
        if i < j: A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

A = list(map(int, input().split()))
quickSort(0, len(A)-1)
print(A)