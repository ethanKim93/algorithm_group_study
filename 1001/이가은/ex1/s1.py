# 반복을 이용한 선택 정렬
# A = [88, 12, 46, 48, 32, 65, 48, 1, 989, 23, 4, 89]
A = [3,4,5,1,2]
def select_sort(A):
    n = len(A)
    for i in range(n-1):
        mini = i
        for j in range(i,n):
            if A[j] < A[mini]:
                mini = j
        A[i], A[mini] = A[mini], A[i]
    return A


def recu_sel_sort(i, A):

    min_v = i

    if i == len(A):
        return print(A)

    else:
        for j in range(i+1,len(A)):
            if A[j] < A[min_v]:
                min_v = j
        A[i], A[min_v] = A[min_v], A[i]
        recu_sel_sort(i+1, A)

print(recu_sel_sort(0, A))

