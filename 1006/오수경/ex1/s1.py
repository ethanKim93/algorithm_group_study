# 배열의 데이터를 퀵 정렬하는 함수를 작성하고 테스트 해보시오.

# Hoare-Partiton
def Hoare_partition(A, l, r):
    p = A[l]
    i = l
    j = r

    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1

        if i < j:
            A[i], A[j] = A[j], A[i]

    A[l], A[j] = A[j], A[l]
    return j



# Lomuto partition
def Lomuto(A, l, r):
    x = A[r]
    i = l-1

    for j in range(l, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i + 1



def quick_sort(A, l, r):
    if l < r:
        # s = Hoare_partition(A, l, r)
        s = Lomuto(A, l, r)

        quick_sort(A, l, s-1)
        quick_sort(A, s+1, r)
    return A


print(quick_sort([11, 45, 23, 81, 28, 34], 0, 5))
print(quick_sort([11, 45, 22, 81, 23, 34, 99, 22, 17, 8], 0, 9))
print(quick_sort([1, 1, 1, 1, 1, 0, 0, 0, 0, 0], 0, 9))